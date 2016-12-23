#!/usr/bin/env python


import logging

LOG_LEVEL = logging.INFO
ZIP_OUTPUT = True

repo_name = 'wam'
repo_path = './../../aac-repos/' + repo_name
base_uri = 'http://data.thewalters.org/'
context_uri = 'https://github.com/american-art/aac-alignment/blob/master/karma-context.json'
REPO_CONFIG = [
    {
        'path': repo_path,
        'name': 'WAM_AAC_Constituents',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'WAM_AAC_Culture-model.ttl',
        'input_file': 'WAM_XMLExport_AAC_Constituents_V3.xml',
        'input_file_type': 'xml',
        'output_file_name': 'WAM_AAC_Culture'
    },
    {
        'path': repo_path,
        'name': 'WAM_AAC_Constituents',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'WAM_AAC_Institution-model.ttl',
        'input_file': 'WAM_XMLExport_AAC_Constituents_V3.xml',
        'input_file_type': 'xml',
        'output_file_name': 'WAM_AAC_Institution'
    },
    {
        'path': repo_path,
        'name': 'WAM_AAC_Constituents',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'WAM_AAC_Individual_PlaceofBirth-model.ttl',
        'input_file': 'WAM_XMLExport_AAC_Constituents_V3.xml',
        'input_file_type': 'xml',
        'output_file_name': 'WAM_AAC_Individual_PlaceofBirth'
    },
    {
        'path': repo_path,
        'name': 'WAM_AAC_Constituents',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'WAM_AAC_Individual_PlaceofDeath-model.ttl',
        'input_file': 'WAM_XMLExport_AAC_Constituents_V3.xml',
        'input_file_type': 'xml',
        'output_file_name': 'WAM_AAC_Individual_PlaceOfDeath'
    },
    {
        'path': repo_path,
        'name': 'WAM_AAC_Constituents',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'WAM_AAC_Individual_PlaceofWork-model.ttl',
        'input_file': 'WAM_XMLExport_AAC_Constituents_V3.xml',
        'input_file_type': 'xml',
        'output_file_name': 'WAM_AAC_Individual_PlaceOfWork'
    },
    {
        'path': repo_path,
        'name': 'WAM_AAC_Dimensions',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'WAM_AAC_Dimensions-model.ttl',
        'input_file': 'WAM_XMLExport_AAC_Dimensions.xml',
        'input_file_type': 'xml',
        'output_file_name': 'WAM_AAC_Dimensions'
    },
    {
        'path': repo_path,
        'name': 'WAM_AAC_Exhibitions',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'WAM_AAC_Exhibitions-model.ttl',
        'input_file': 'WAM_XMLExport_AAC_Exhibitions.xml',
        'input_file_type': 'xml',
        'output_file_name': 'WAM_AAC_Exhibitions'
    },
    {
        'path': repo_path,
        'name': 'WAM_AAC_Geography',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'WAM_AAC_Geography-PlaceOfOrigin-model.ttl',
        'input_file': 'WAM_XMLExport_AAC_Geography.xml',
        'input_file_type': 'xml',
        'output_file_name': 'WAM_AAC_Geography_PlaceOfOrigin'
    },
    {
        'path': repo_path,
        'name': 'WAM_AAC_Media',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'WAM_AAC_Media-model.ttl',
        'input_file': 'WAM_XMLExport_AAC_Media_v3.xml',
        'input_file_type': 'xml',
        'output_file_name': 'WAM_AAC_Media'
    },
    {
        'path': repo_path,
        'name': 'WAM_AAC_Objects',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'WAM_AAC_Objects-model.ttl',
        'input_file': 'WAM_XMLExport_AAC_Objects.xml',
        'input_file_type': 'xml',
        'output_file_name': 'WAM_AAC_Objects'
    },
    {
        'path': repo_path,
        'name': 'WAM_AAC_Titles',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'WAM_AAC_Titles-model.ttl',
        'input_file': 'WAM_XMLExport_AAC_Titles_v2_11-2016.xml',
        'input_file_type': 'xml',
        'output_file_name': 'WAM_AAC_Titles'
    },
    {
        'path': repo_path,
        'name': 'WAM_AAC_Titles',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'WAM_AAC_OtherTitles-model.ttl',
        'input_file': 'WAM_XMLExport_AAC_Titles_v2_11-2016.xml',
        'input_file_type': 'xml',
        'output_file_name': 'WAM_AAC_OtherTitles'
    }

]