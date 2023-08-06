import os

import nkdv
import osmnx as ox
import numpy as np
import pandas as pd
from io import StringIO
import sys
import networkx as nx
from shapely.geometry import Point
from shapely.geometry import LineString
import geopandas as gpd
import processing
from processing.core.Processing import Processing
import matplotlib.pyplot as plt


def setPath(processing_path):
    for i in processing_path:
        sys.path.append(i)


def process_edges(graph):
    edge_list = []
    for edge in graph.edges:
        node1_id = edge[0]
        node2_id = edge[1]
        length = graph[node1_id][node2_id][0]['length']
        edge_list.append([node1_id, node2_id, length])
    return pd.DataFrame(edge_list, columns=['u_id', 'v_id', 'length'])


def project_data_points_and_generate_points_layer(graph, nodes, filename):
    longitudes = nodes[:, 0]
    latitudes = nodes[:, 1]
    points_list = [Point((lon, lat)) for lon, lat in zip(longitudes, latitudes)]  # turn into shapely geometry
    points = gpd.GeoSeries(points_list,
                           crs='epsg:4326')  # turn into GeoSeries
    points.to_file('points_layer_' + filename + '.gpkg')
    points_proj = points.to_crs(graph.graph['crs'])

    xs = [pp.x for pp in points_proj]
    ys = [pp.y for pp in points_proj]
    nearest_edges = ox.nearest_edges(graph, xs, ys)
    distances = []
    projected_point_list = []
    # project data points respectively
    for i in range(len(longitudes)):
        if i % 10000 == 0:
            print("current point: ", i)

        point1_id = nearest_edges[i][0]  # the nearest edge's source node's node id
        point2_id = nearest_edges[i][1]  # the nearest edge's target node's node id

        # generate projection on nearest edge
        data_point = Point(xs[i], ys[i])  # one data point to be projected
        edge = graph.get_edge_data(nearest_edges[i][0], nearest_edges[i][1])[0]['geometry']

        projected_dist = edge.project(data_point)
        projected_point = edge.interpolate(projected_dist)
        projected_point_list.append(projected_point)

        distances.append([point1_id, point2_id, projected_dist])

    points = gpd.GeoSeries(projected_point_list, crs=graph.graph['crs'])
    projected_points = points.to_crs(4326)
    projected_points.to_file('projected_points_layer.gpkg')
    distances_df = pd.DataFrame(distances, columns=['u_id', 'v_id', 'distance'])
    distances_df = distances_df.sort_values(by=['u_id', 'v_id', 'distance'], ascending=[True, True, True],
                                            ignore_index=True)

    return distances_df


def fix_direction(graph):
    x_dic = {}
    for i, node in enumerate(graph.nodes(data=True)):
        x_dic[i] = node[1]['x']
    for i, edge in enumerate(graph.edges(data=True)):
        shapely_geometry = edge[2]['geometry']
        x, y = shapely_geometry.xy
        if abs(x[0] - x_dic[edge[0]]) > 0.00001:  # edge0 is u (source ID)
            edge[2]['geometry'] = shapely_geometry.reverse()


def merge(edges_df, dis_df, nodes_num, graph_output_name):
    # df1 is edge dataframe and df2 is distance dataframe
    merge_df = pd.merge(edges_df, dis_df, on=['u_id', 'v_id'], how='left')
    merge_df = merge_df.sort_values(by=['u_id', 'v_id'], ascending=[True, True])
    merge_df = merge_df.reset_index()
    merge_np = merge_df.to_numpy()
    if np.isnan(merge_np[0][4]):  # or we can use merge_np[0][4]>0
        row = [merge_np[0][1], merge_np[0][2], merge_np[0][3], 0]
    else:
        row = [merge_np[0][1], merge_np[0][2], merge_np[0][3], 1, merge_np[0][4]]
    res = []
    for i in range(1, merge_np.shape[0]):
        if merge_np[i][1] == merge_np[i - 1][1] and merge_np[i][2] == merge_np[i - 1][2]:
            row[3] = row[3] + 1
            row.append(merge_np[i][4])
        elif np.isnan(merge_np[i][4]):
            res.append(row)
            row = [merge_np[i][1], merge_np[i][2], merge_np[i][3], 0]
        else:
            res.append(row)
            row = [merge_np[i][1], merge_np[i][2], merge_np[i][3], 1, merge_np[i][4]]
    res.append(row)
    with open(graph_output_name, 'w') as fp:
        fp.write("%s " % str(nodes_num))
        fp.write("%s\n" % str(edges_df.shape[0]))
        for list_in in res:
            fp.write("%s " % str(int(list_in[0])))
            fp.write("%s" % str(int(list_in[1])))
            for i in range(2, len(list_in)):
                # write each item on a new line
                fp.write(" %s" % str(list_in[i]))
            fp.write("\n")


def buildGraphFromPoints(path_from):
    nodes = np.genfromtxt(path_from, delimiter=' ')
    longitudes = nodes[:, 0]
    latitudes = nodes[:, 1]

    points_list = [Point((lng, lat)) for lat, lng in zip(latitudes, longitudes)]
    points = gpd.GeoSeries(points_list, crs='epsg:4326')
    points.to_file('points_layer.gpkg')


def add_kd_value(gdf, value_se, to_file):
    columns_list = gdf.columns.tolist()
    columns_list.append('value')
    gdf = gdf.reindex(columns=columns_list)
    gdf['value'] = value_se
    gdf.to_file(to_file)
    return gdf
    # gdf.plot()


def update_length(df1, df2):
    print(df1.info())
    print(df2.info())
    df1['length'] = df2['length']


def map_road_network(location_data):
    # qgs = QgsApplication([], False)
    # qgs.initQgis()
    Processing.initialize()
    (data_file_path, data_file_name) = os.path.split(location_data)
    if '.' in data_file_name:
        data_file_name = data_file_name.split('.')[0]
    data_arr = np.genfromtxt(location_data, delimiter=' ')
    data_df = pd.DataFrame(data_arr, columns=['lon', 'lat'])
    # data cleaning
    # data_df = data_df[(np.abs(stats.zscore(data_df)) < 4).all(axis=1)]
    lat_max = data_df['lat'].max()
    lat_min = data_df['lat'].min()
    lon_max = data_df['lon'].max()
    lon_min = data_df['lon'].min()
    print(lat_max, lat_min, lon_max, lon_min)
    print('start downloading map')
    g1 = ox.graph_from_bbox(lat_max, lat_min, lon_max, lon_min, simplify=True, network_type='drive')
    gc1 = ox.consolidate_intersections(ox.project_graph(g1), tolerance=20, rebuild_graph=True)
    undi_gc1 = gc1.to_undirected()
    single_undi_gc1 = nx.Graph(undi_gc1)
    g = nx.MultiGraph(single_undi_gc1)
    nodes_num = g.number_of_nodes()
    fix_direction(g)
    print('start processing edges')
    edge_df = process_edges(g)
    geo_path_1 = 'geo1.gpkg'
    ox.save_graph_geopackage(g, geo_path_1)
    df1 = gpd.read_file(geo_path_1, layer='edges')
    geo_path_2 = 'simplified_' + data_file_name + '.gpkg'
    df1 = df1[['geometry']]
    df1.to_file(geo_path_2, driver='GPKG', layer='edges')

    added_geometry_filename = 'add_geometry.shp'
    processing.run("qgis:exportaddgeometrycolumns",
                   {'INPUT': geo_path_2 + '|layername=edges', 'CALC_METHOD': 0, 'OUTPUT': added_geometry_filename})

    df2 = gpd.read_file(added_geometry_filename)
    update_length(edge_df, df2)

    print('start projecting points to the road')
    distance_df = project_data_points_and_generate_points_layer(g, data_arr, data_file_name)
    graph_output_name = 'graph_output_' + data_file_name
    merge(edge_df, distance_df, nodes_num, graph_output_name)
    road_data = [geo_path_2, graph_output_name]
    return road_data


def output(results, output_file_name):
    df4 = gpd.read_file(results[1])
    df5 = pd.read_csv(results[0], sep=',', skiprows=1, names=['value'])['value']
    if '.shp' not in output_file_name:
        output_file_name += '.shp'
    add_kd_value(df4, df5, output_file_name)
    # output_gdf.to_crs(4326, inplace=True)
    # output_gdf.plot('value', cmap='OrRd', legend=True)
    # plt.show()


class PyNKDV:
    def __init__(self, road_data, bandwidth=1000, lixel_size=5, num_threads=8):
        self.graph_path = road_data[0]
        self.data_file = road_data[1]
        self.bandwidth = bandwidth
        self.lixel_size = lixel_size
        self.num_threads = num_threads

    def compute(self):
        Processing.initialize()
        qgis_split_output = 'split_by_qgis.shp'
        print('start splitting roads')
        processing.run("native:splitlinesbylength", {
            'INPUT': self.graph_path + '|layername=edges',
            'LENGTH': self.lixel_size, 'OUTPUT': qgis_split_output})

        example = nkdv.NKDV(bandwidth=self.bandwidth, lixel_reg_length=self.lixel_size, method=3)
        example.set_data(self.data_file)
        example.compute()
        result_io = StringIO(example.result)
        df_cplusplus = pd.read_csv(result_io, sep=' ', skiprows=1, names=['a', 'b', 'c', 'value'])['value']
        c_output_path = 'kde_output_b' + str(self.bandwidth) + '_l' + str(self.lixel_size)
        df_cplusplus.to_csv(c_output_path)
        result = [c_output_path, qgis_split_output]
        return result
        # add_kd_value(df4, series_cplusplus, final_output_path)
