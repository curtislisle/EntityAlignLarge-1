import json
import tangelo

tangelo.paths('.')
from lineupdataset import translate


def run(displaymode):
    # Create an empty response object.
    response = {}

    if displaymode in ('left network only', 'right network only'):
        print 'displaying left or right'
        # return fixed result to compare two datasets
        response['primaryKey'] = 'full_name'
        response['separator'] = '\t'
        response['url'] = 'service/lineupdataset'
        response['columns'] = [
            {'column': 'full_name', 'type': 'string'},
            {'column': 'role', 'type': 'string'},
            {'column': 'gender', 'type': 'string'},
            {'column': 'numberOfCoAuthors', 'type': 'number', 'domain': [0, 50]},
            {'column': 'percentage_female', 'type': 'number', 'domain': [0, 1]},
            {'column': 'totalPublications', 'type': 'number', 'domain': [0, 225]}]
        response['layout'] = {'primary': [
            {'column': 'full_name', 'width': 130},
            {'column': 'role', 'width': 80},
            {'column': 'gender', 'width': 80},
            {'column': 'numberOfCoAuthors', 'width': 100},
            {'column': 'percentage_of_female', 'width': 100},
            {'column': 'totalPublications', 'width': 100},
            {'type': 'stacked', 'label': 'Combined', 'children': [
                {'column': '1hop', 'width': 75},
                {'column': '2hop', 'width': 75}]}]}
    else:
        # return fixed result to compare two datasets
        print 'displaying centered'
        response['primaryKey'] = 'full_name'
        response['separator'] = '\t'
        response['url'] = 'service/lineupdataset'
        response['columns'] = [
            {'column': translate['full_name'], 'type': 'string'},
            {'column': translate['role'], 'type': 'string'},
            {'column': translate['gender'], 'type': 'string'},
            {'column': translate['aspt_member'], 'type': 'number','domain': [0, 1]},            
            {'column': translate['numberOfCoAuthors'], 'type': 'number', 'domain': [0, 60]},
            {'column': translate['OneHopSize'], 'type': 'number', 'domain': [0, 60]},
            {'column': translate['percentage_female'], 'type': 'number', 'domain': [0, 1]},
            {'column': translate['totalPublications'], 'type': 'number', 'domain': [0, 300]},
            {'column': translate['betweenness'], 'type': 'number', 'domain': [0, 0.1]}]
        response['layout'] = {
            'primary': [
                {'column': translate['full_name'], 'width':100},
                {'column': translate['role'], 'width':60},
                {'column': translate['gender'], 'width':40},  
                {'type': 'stacked', 'label': 'Combined', 'children': [
                    {'column': translate['aspt_member'], 'width': 40},
                    {'column': translate['numberOfCoAuthors'], 'width':50},
                    {'column': translate["OneHopSize"], 'width':50},
                    {'column': translate['betweenness'], 'width': 70},
                    {'column': translate['percentage_female'], 'width': 90},
                    {'column': translate['totalPublications'], 'width': 60}]}]}

    # tangelo.log(str(response))
    return json.dumps(response)
