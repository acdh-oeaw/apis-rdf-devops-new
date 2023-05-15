#!/bin/bash
if [[ "${APIS_RDF_ONTOLOGY}" ]]; then
	ln -s ${APIS_RDF_ONTOLOGY} apis_ontology
	pip install -r ${APIS_RDF_ONTOLOGY}/requirements.txt
fi
gunicorn wsgi -b 0.0.0.0:5000 --timeout 120 --workers=3 --threads=3 --worker-connections=1000