# Automation Service 

The Automation Service offers the possibility to have an automatically
generated model based on its given data and endpoints to interact with
it. In this file, the examples given will follow a NER concerning names,
s.t., it tries to identify *Firstnames*, *Middlenames*, and *Lastnames*.
However, you may define any entities to recognize that you want. A demo
of the service can be accessed at <http://demos.swe.htwk-leipzig.de>.

The service can be run as standalone or within a [Qanary-driven Question
Answering system](https://github.com/WDAqua/Qanary).

Starting Conditions
===================

There are two options (requirements) for starting the service:

-   option 1: a pre-trained model, or

-   option 2: there must be either compatible datasets for training and
    testing.

Option 1
--------

If a pre-trained model is intended to be provided, it must be available
in the folder
[AutomationService/AutomationServiceBackend/data/model](./AutomationService/AutomationServiceBackend/data/model)
(default configuration). The service works only with
[spaCy](https://spacy.io) models. Hence, your model needs to follow the
spaCy standards (or should be trained using spaCy). In a netconsole,
just copy the contents of a trained model (usually in the folder
`model-best` or `model-last`) into the mentioned folder.

Option 2
--------

If no pre-trained model is provided, training and testing data must be
provided to the system. Otherwise, the web service will not start. Both
files must be provided in the folder
[AutomationService/AutomationServiceBackend/data/trainingdata](./AutomationService/AutomationServiceBackend/data/trainingdata).
Additionally, the file names must be defined in the
[.env](./AutomationService/.env) file. Both datasets must always be in
CSV file format and meet the following requirements:

-   Each file contains columns for the input-text (first column) and
    each entity the model should be able to identify.

-   Then, each data-text is written into the text-column and
    additionally, the values for each entity inside the text are defined
    separately in the respective column.

-   If a text does not contain a value for a defined entity, the
    corresponding cell must be empty.

An example for an [exemplary CSV-formatted dataset for recognizing names
of people](./AutomationService/ExampleBodies/name) would be something
like this:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th>Name</th>
<th>First_Name</th>
<th>Middle_Name</th>
<th>Last_Name</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>I am Ms Walters</p></td>
<td></td>
<td></td>
<td><p>Walters</p></td>
</tr>
<tr class="even">
<td><p>Do you think Silke will come?</p></td>
<td><p>Silke</p></td>
<td></td>
<td><p>startquestionansweringwithtextquestion</p></td>
</tr>
<tr class="odd">
<td><p>I do have a middlename, it’s Heinz-Wilhelm</p></td>
<td></td>
<td><p>Heinz-Wilhelm</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>You can send the data to Ingetraut Renz</p></td>
<td><p>Ingetraut</p></td>
<td></td>
<td><p>Renz</p></td>
</tr>
</tbody>
</table>

When generating the training data, there can only be one of each entity
type given. The training process will not work for multiple. However,
the later model has the code-setup to recognize and work with multiple
results.n

Training and testing data must follow the same basic structure (i.e.,
they must have the same column name).

There are two example environments files given for initial training with
[name](./.env.template-name-training) or
[address](./.env.template-address-training) data.

Starting the Service
====================

To start the service, docker-compose files are provided. Therefore, you
need to have docker and docker-compose installed. Additionally, if you
want to use a GPU to train the models, you might need additional
requirements based on your drivers / hardware, if not you need to remove
the lines from the docker-compose. Refer to the documentation needed for
these. Nothing else is needed.

Starting as a standalone Service
--------------------------------

If you want to run the service as a standalone, in the root directory
build the images. Please note that if the service runs as a standalone,
it will be running on the port *8002* per default as opposed to 8080 and
8081.

    docker-compose -f docker-compose_standalone.yml build

You can then run the service via:

    docker-compose -f docker-compose_standalone.yml up

Add `-d` to the call to have it run in the background and not be bound
by the running console.

Starting a Qanary Environment
-----------------------------

### Starting a complete Qanary environment

If you want to run the service as a Qanary component, in the root
directory build the images for it. The setup in the docker-compose
automatically creates a Qanary instance as well as a Stardog server to
interact with.

    docker-compose -f docker-compose_qanary-example-local-stardog.yml build

You can then run it via:

    docker-compose -f docker-compose_qanary-example-local-stardog.yml up

Add `-d` to the call to have it run in the background and not be bound
by the running console.

Using the file `docker-compose-full-example.yml` will connect the
pipeline automatically to the HTWK Stardog server.

### How to start the service and connect it to an existing Qanary Question Answering System

If you already have a Qanary pipeline, you might just want to add the
component to it. In this case, you can build and start only the required
component. To do this, the following commaned is used:

    docker-compose -f docker-compose_QanaryComponent.yml build automation_component

You can then run it via:

    docker-compose -f docker-compose_QanaryComponent.yml up automation_component

Add `-d` to the call to have it run in the background and not be bound
by the running console.

However, in that case additional configurations are needed to be done.
To connect the service to an existing Qanary pipeline, the following
steps must be taken:

-   In the highest [.env](./AutomationService/.env) file, the following
    values have to be adjusted:

    -   `SPRING_BOOT_ADMIN_URL`

    -   `SPRING_BOOT_ADMIN_USERNAME`

    -   `SPRING_BOOT_ADMIN_PASSWORD`

-   In the same file, the component connection settings have to be
    adjusted:

    -   `SERVICE_HOST`

    -   `SERVICE_PORT`

-   You can also find the component name and description in this file

To connect the service with an already existing ML Flow Logger, the
following steps must be taken:

-   In the [.env](./AutomationService/AutomationServiceBackend/app/.env)
    file of the component, the following values have to be adjusted:

    -   `MLFLOW_URI`

-   In the same file, if SFTP is used, the following values have to be
    adjusted:

    -   `USE_SFTP = True`

    -   `MLFLOW_HOST`

    -   `MLFLOW_PORT`

-   In the highest [.env](./AutomationService/.env) file, the ML FLOW
    Logger values are only relevant for the complete system and do not
    need to be paid attention to for the standalone component

Possible errors
---------------

### `Additional properties are not allowed ('devices' was unexpected)`

The full error message might look like this:

    ERROR: The Compose file './docker-compose_QanaryComponent.yml' is invalid because: services.automation_component.deploy.resources.reservations value Additional properties are not allowed ('devices' was unexpected)

Reason: The prepared docker-compose file is integrating GPU
capabilities. Following the [Docker
documentation](https://docs.docker.com/compose/gpu-support/#enabling-gpu-access-to-service-containers),
to take advantage of this functionality you need at least docker-compose
version v1.28.0+ (check by running the command:
`docker-compose --version`).

You might install the most recent version using pip:

    pip install docker-compose --upgrade

### `Parameters not supported in API versions < X`

The full error message might look like this:

    ERROR: for automation_component  device_requests param is not supported in API versions < 1.40

Reason: the docker-compose version used is too outdated. In building
this service, the lowest used version was `2.12.2` which worked fine. IF
the error occurs, you might install the newest docker-compose version
using your preferred installation method.

On Arch Linux, the call to install / update docker compose would be:

    sudo pacman -S docker-compose

For Ubuntu and Debain you can run:

    sudo apt-get install docker-compose-plugin

Interaction with the Service
============================

Once a Qanary service is started, you may interact with it through a
handful of endpoints offered as APIs that will either provide access to
some way of information extraction from the given data or enable you to
retrain (i.e., exchange) the model on runtime.

Qanary endpoint
---------------

To interact with the Qanary interface, you can access it using the
following webpage:

    http://demos.swe.htwk-leipzig.de:40111/startquestionansweringwithtextquestion

It allows you to ask questions and the recognized entities will be saved
in the Stardog server. The page also allows you to interact with
Stardog.

If you enter a question such as "My name is Annemarie Wittig." with the
default model, there will be two annotations created, one for the first-
and one for the last name. The generated query will be something like
this:

    PREFIX dbr: <http://dbpedia.org/resource/
    PREFIX dbo: <http://dbpedia.org/ontology/
    PREFIX qa: <http://www.wdaqua.eu/qa#
    PREFIX oa: <http://www.w3.org/ns/openannotation/core/
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#
    INSERT {
    GRAPH <urn:graph:6ddac4c3-fbc1-4016-a107-d9126b806b65  {
        ?entityAnnotation0 a qa:AnnotationOfInstance .
        ?entityAnnotation0 oa:hasTarget [
            a   oa:SpecificResource;
                oa:hasSource    <http://localhost:8080/question/stored-question__text_dc03e843-a2bf-4de0-aec0-280fc8d4adb1  ;
                oa:hasSelector  [
                    a oa:TextPositionSelector ;
                    oa:start "11"^^xsd:nonNegativeInteger ;
                    oa:end  "20"^^xsd:nonNegativeInteger
                ]
            ] .
        ?entityAnnotation0 oa:hasBody "FIRST_NAME"^^xsd:string ;
            oa:annotatedBy <urn:qanary:AutomationServiceComponent  ;
            oa:annotatedAt ?time ;
            qa:score "0.5"^^xsd:decimal .

        ?entityAnnotation1 a qa:AnnotationOfInstance .
        ?entityAnnotation1 oa:hasTarget [
            a   oa:SpecificResource;
                oa:hasSource    <http://localhost:8080/question/stored-question__text_dc03e843-a2bf-4de0-aec0-280fc8d4adb1  ;
                oa:hasSelector  [
                    a oa:TextPositionSelector ;
                    oa:start "21"^^xsd:nonNegativeInteger ;
                    oa:end  "27"^^xsd:nonNegativeInteger
                ]
            ] .
        ?entityAnnotation1 oa:hasBody "MIDDLE_NAME"^^xsd:string ;
            oa:annotatedBy <urn:qanary:AutomationServiceComponent  ;
            oa:annotatedAt ?time ;
            qa:score "0.5"^^xsd:decimal .
        }
    }
    WHERE {
        BIND (IRI(str(RAND())) AS ?entityAnnotation0) .
        BIND (IRI(str(RAND())) AS ?entityAnnotation1) .
        BIND (now() as ?time)
    }

Querying data from the Qanary triplestore with a query like the
following, will return the NER parts of the annotation:

    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#
    PREFIX oa: <http://www.w3.org/ns/openannotation/core/
    PREFIX qa: <http://www.wdaqua.eu/qa#
    SELECT *
    FROM <urn:graph:6ddac4c3-fbc1-4016-a107-d9126b806b65
    WHERE {
        ?annotationId rdf:type ?type.
        ?annotationId oa:hasBody ?body.
        ?annotationId oa:hasTarget ?target.
        ?target oa:hasSelector ?selector .
        ?selector oa:start ?start .
        ?selector oa:end ?end .
    }

The result then looks like this:

![Example
Result](https://user-images.githubusercontent.com/59013332/197013196-6cce4c8b-07d9-4426-aaa7-53fe753905c6.png)

Alternatively, you can curl against the pipeline directly using a curl
command such as:

    curl --location --request POST 'http://demos.swe.htwk-leipzig.de:40170/questionanswering?textquestion=Who is Barack Obama?&language=en&componentlist%5B%5D=AutomationServiceComponent'

NER Endpoint
------------

### /api

The /api endpoint offers two interfaces for interaction.

#### GET

The GET interface offers the possibility to retrieve the NER of a single
text by your model. This is only an endpoint for quick result checks and
does not allow mlflow logging. You can interact with it by using a call
like:

    curl -X 'GET' 'http://demos.swe.htwk-leipzig.de:40170/api?text=TEXT'

Remember to replace spaces with *%*. The result will be the original
text, recognized entities with their labels and content:

    [
        {
            "text": "text",
            "results": [
                {
                    "Entity-Label1": "value1",
                    "Entity-Label2": "value2"
                }
            ]
        }
    ]

#### POST

The POST interface offers a NER for multiple input possibilities:

1.  upload a CSV file,

2.  upload a JSON file, or

3.  upload raw JSON data within the body of your request.

In all cases the matching
["accept"-header](https://developer.mozilla.org/docs/Web/HTTP/Headers/Accept)
must be set within the HTTP request. It will define whether the output
is of the type `application/json` or `text/csv`. If another or an
invalid "accept"-header is given, the service will either use the
["Content-Type"-header](https://developer.mozilla.org/docs/Web/HTTP/Headers/Content-Type)
of the uploaded file or, if no file was uploaded, it will use it from
the request. If none of these are valid, the request will fail. Hence,
if you consider problems, then add or check the headers that are defined
in your Web service request.

You can also send the parameter `use_ml_logger` with the value `True`
with these request to activate logging using mlflow. This is
*recommended* while using the component in a real Question Answering
system to establish a tracking of the component’s behavior (i.e., the
quality).

====== CSV Upload

You can upload a CSV file, containing texts that are supposed to be run
through NER in the first column, to the Web service. There can be any
other columns added if required. For example, the expected entities
could be added to compare expected and actual results. The service will
then annotate the CSV file with columns for all its recognizable
entities and fill these up with the entities contained in each row. The
`curl` command would be:

    curl -X POST -H 'accept: application/json' -F "file_to_identify=@{YOUR CSV FILE PATH};type=text/csv" http://demos.swe.htwk-leipzig.de:40170/api

The service will answer with the annotated CSV file. Additionally, the
response file will also be saved locally in the container in the folder
`/code/app/spacy_model/intermediate/results/`.

As an example, if you want to upload a file such as:

<table style="width:100%;">
<colgroup>
<col style="width: 51%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th>Text</th>
<th>First_Name</th>
<th>Middle_Name</th>
<th>Last_Name</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>People call me Ida Clayton Henderson</p></td>
<td><p>Ida</p></td>
<td><p>Clayton</p></td>
<td><p>Henderson</p></td>
</tr>
<tr class="even">
<td><p>I am happy to meet you, too. You can call me Kira.</p></td>
<td><p>Kira</p></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><p>You can send the data to Eberhard Rump</p></td>
<td><p>Eberhard</p></td>
<td></td>
<td><p>Rump</p></td>
</tr>
<tr class="even">
<td><p>Please send all business inquiries to Jessie Edwin Fowler</p></td>
<td><p>Jessie</p></td>
<td><p>Edwin</p></td>
<td><p>Fowler</p></td>
</tr>
<tr class="odd">
<td><p>Oh, I actually go by Lioba Alexandra.</p></td>
<td><p>Lioba</p></td>
<td><p>Alexandra</p></td>
<td></td>
</tr>
</tbody>
</table>

with `text/csv` as an "accept"-header, it would result in something
like:

<table style="width:100%;">
<colgroup>
<col style="width: 33%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th>Text</th>
<th>First_Name</th>
<th>Middle_Name</th>
<th>Last_Name</th>
<th>FIRST_NAME</th>
<th>LAST_NAME</th>
<th>MIDDLE_NAME</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>People call me Ida Clayton Henderson</p></td>
<td><p>Ida</p></td>
<td><p>Clayton</p></td>
<td><p>Henderson</p></td>
<td><p>Ida</p></td>
<td><p>Henderson</p></td>
<td><p>Clayton</p></td>
</tr>
<tr class="even">
<td><p>I am happy to meet you, too. You can call me Kira.</p></td>
<td><p>Kira</p></td>
<td></td>
<td></td>
<td><p>Kira</p></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><p>You can send the data to Eberhard Rump</p></td>
<td><p>Eberhard</p></td>
<td></td>
<td><p>Rump</p></td>
<td><p>Eberhard</p></td>
<td><p>Rump</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>Please send all business inquiries to Jessie Edwin Fowler</p></td>
<td><p>Jessie</p></td>
<td><p>Edwin</p></td>
<td><p>Fowler</p></td>
<td><p>Jessie</p></td>
<td><p>Fowler</p></td>
<td><p>Edwin</p></td>
</tr>
<tr class="odd">
<td><p>Oh, I actually go by Lioba Alexandra.</p></td>
<td><p>Lioba</p></td>
<td><p>Alexandra</p></td>
<td></td>
<td><p>Lioba</p></td>
<td></td>
<td><p>Alexandra</p></td>
</tr>
</tbody>
</table>

However, having defined the `accept`-header as `application/json`. The
response of the Web service would be:

    [
        {
            "text": "People call me Ida Clayton Henderson",
            "entities": [
                {
                    "First_Name": "Ida",
                    "Middle_Name": "Clayton",
                    "Last_Name": "Henderson"
                }
            ],
            "results": [
                {
                    "FIRST_NAME": "Ida",
                    "LAST_NAME": "Henderson",
                    "MIDDLE_NAME": "Clayton"
                }
            ]
        },
        {
            "text": "I am happy to meet you, too. You can call me Kira.",
            "entities": [
                {
                    "First_Name": "Kira",
                    "Middle_Name": null,
                    "Last_Name": ""
                }
            ],
            "results": [
                {
                    "FIRST_NAME": "Kira",
                    "LAST_NAME": "",
                    "MIDDLE_NAME": ""
                }
            ]
        },
        ...
    ]

====== JSON File Upload

Additionally, the endpoint allows applying NER to all texts given in a
JSON file much like the [CSV Upload](#csv-upload). The JSON file must
follow this structure:

    [
        {
            "text": "{TEXT TO CLASSIFY}",
            "language": "{LANGUAGE}",
            "entities": {
                "{ENTITY1}": "{VALUE1}",
                "{ENTITY2}": "{VALUE2}",
                ...
            }
        }
    ]

However, both the language and the entity tags can be left out (they
default to null), if wanted. The NER via uploading a JSON file, much
like the CSV file upload, allows the freedom to add any additional
information that is wanted, as long as each object has the "attribute
text". Hence, request data of sending two element might look like:

    [
        {
            "text": "{TEXT TO CLASSIFY}"
        },
        {
            "text": "{TEXT TO CLASSIFY}"
        }
    ]

Example files to upload are the texts.json files found in the folder
[./AutomationService/ExampleBodies/name](./AutomationService/ExampleBodies/name)
and
[./AutomationService/ExampleBodies/address](./AutomationService/ExampleBodies/address)
directories.

A corresponding `curl` call would be:

    curl -X POST -H 'accept: application/json' -F "file_to_identify=@{YOUR JSON FILE PATH};type=application/json" http://demos.swe.htwk-leipzig.de:40170/api

The response will be the annotated JSON, but it will also be stored
locally in the container. It can be found as
`/code/app/spacy_model/intermediate/results/`. The NER results can be
found in the `results` array. An example response object looks like
this:

    [
        {
            "text": "I am called Marilyn Monroe.",
            "language": "en",
            "entities": [
                {
                    "First_Name": "Marilyn",
                    "Last_Name": "Monroe"
                }
            ],
            "results": [
                {
                    "FIRST_NAME": "Marilyn",
                    "LAST_NAME": "Monroe"
                }
            ]
        }
    ]

If this was entered with `text/csv` as `accept`-header, the result would
be:

<table>
<colgroup>
<col style="width: 38%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th>text</th>
<th>language</th>
<th>entities_First_Name</th>
<th>entities_Last_Name</th>
<th>results_FIRST_NAME</th>
<th>results_LAST_NAME</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>I am called Marilyn Monroe.</p></td>
<td><p>en</p></td>
<td><p>Marilyn</p></td>
<td><p>Monroe</p></td>
<td><p>Marilyn</p></td>
<td><p>Monroe</p></td>
</tr>
</tbody>
</table>

====== Raw JSON Upload

The direct upload works exactly as the [JSON File
Upload](#json-file-upload) with the difference, that the request body is
not a file but the JSON data as a string. It has the same structure and
response as in the JSON File Upload and all additional information can
be referenced there. The only difference is the `curl` command, which
will look something like this:

    curl -X POST -H 'accept: application/json' -H "Content-Type: application/json" -d '{{YOUR JSON}}' http://demos.swe.htwk-leipzig.de:40170/api

Or an example of a `curl` with content:

    curl -X 'POST' \
    'http://demos.swe.htwk-leipzig.de:40170/api' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '[
        {
            "text": "I am called Marilyn Monroe.",
            "language": "en",
            "entities": {
                "First_Name": "Marilyn",
                "Last_Name": "Monroe"
                }
            }
    ]'

Alternatively, the `accept`-header can be set to CSV, too.

Retrain Endpoint
----------------

The retraining endpoint uses the data you provided to train a new NER
model which will if all is successful, replace the original model. All
following interactions will then be with the new model. **The original
model will be deleted.** "accept"-headers will not be relevant, as the
only return value is a success message in JSON format.

The retraining will, after formatting the input if needed, go through
the [data
preparation](https://github.com/AnnemarieWittig/RecognitionService/blob/main/Documentation/SpaCyTrainingProcess.md)
as it is described in the documentation, save the created intermediate
files within the container and will then use the created docbins to
train a new model. All of this happens in a folder located in the
container as `/code/app/spacy_model/intermediate/`. Once the training
concludes successfully, the files are moved into the system and
overwrite other existing files, either of the original model or the
original intermediate files. Both, the (formatted) training- and
testingdata as well as the generated docbins will be saved in the
container (until overwritten again). The used model will always be the
`model-best` generated by SpaCy.

After the training, you can find your files here: \* Trainingdata is
saved as `train.csv` in `/code/app/spacy_model/corpus/trainingdata/` \*
Testingdata is saved as `test.csv` in
`/code/app/spacy_model/corpus/trainingdata/` \* The generated docbins
are saved as `train.spacy` and `test.spacy` in
`/code/app/spacy_model/corpus/spacy-docbins/` \* The model (only the
contents of the model-best) will be found in
`/code/app/spacy_model/output/model-best/`

Everything else such as the other trained model will be deleted.

Please note that the process of retraining can, depending on your
hardware, take some time to finish. The classification APIs can still be
used with the original model while the training runs.

You can also send the parameter `use_ml_logger` with the value `True`
with these request to activate logging using mlflow. This is recommended
when you use Qanary.

### CSV Upload

The endpoint allows to upload two CSV files, the `trainingdata` and the
`testingdata`, as CSV files. You can name them however you like, as long
as the files have the exact structure as the ones needed in the
[Starting Conditions](#starting-conditions).

The corresponding `curl` call would be:

    curl -X POST -F 'trainingdata=@{YOUR TRAININGDATA CSV};type=text/csv' -F 'testingdata=@{YOUR VALIDATION CSV};type=text/csv' http://demos.swe.htwk-leipzig.de:40170/retrain

### JSON File Upload

The endpoint allows the upload of trainingfiles in JSON format. There
are three files needed in total. The training data is structured like
this:

    {
        "trainingdata": [
            {
                "text": "{TRAININGTEXT}",
                "language": "{LANGUAGETEXT (not relevant for training and can be ignored, language is set in the model config)}",
                "entities": {
                    "{ENTITY1}": "{VALUE1}",
                    "{ENTITY2}": "{VALUE2}",
                    ...
                }
            }
        ]
    }

The data for tests follows the same structure. But, inside the file, the
initial key is named `testingdata` (instead of `trainingsdata`).

For the JSON upload, a third file is needed. It is called options and
contains a list of all possible `entities` the NER is supposed to
recognize as well as the model `language` and `modeltype`. None of these
are optional and they all must be provided. It has the following
structure:

    {
        "entities": ["{ENTITY1}", "{ENTITY2}", ...],
        "language": "en",
        "modeltype": "spacy"
    }

Example files for `curl` commands can be found in the
[ExampleBodies/name](./AutomationService/ExampleBodies/name) and
[ExampleBodies/address](./AutomationService/ExampleBodies/address)
directories.

Warning: Please note that those are minimal examples and will not
generate a well-working NER model.

The following `curl` command would start the retraining of the
component’s model:

    curl -X POST -F 'trainingdata=@{YOUR TRAININGDATA JSON};type=application/json' -F 'testingdata=@{YOUR VALIDATION JSON};type=application/json' -F 'options=@{YOUR OPTIONS JSON};type=application/json' http://demos.swe.htwk-leipzig.de:40170/retrain

### JSON Raw Upload

The `json/upload-direct` endpoint allows the data needed to be retrained
raw within the body of the request. The data itself is structured as is
for the [JSON File Upload](#json-file-upload-1), but all put in one file
like the following:

    {
        "trainingdata": [
            {
                "text": "{TRAININGTEXT}",
                "language": "{LANGUAGETEXT (not relevant for training and can be ignored, language is set in the model config)}",
                "entities": {
                    "{ENTITY1}": "{VALUE1}",
                    "{ENTITY2}": "{VALUE2}",
                    ...
                }
            }
        ],
        "testingdata": [
            {
                "text": "{TRAININGTEXT}",
                "language": "{LANGUAGETEXT (not relevant for training and can be ignored, language is set in the model config)}",
                "entities": {
                    "{ENTITY1}": "{VALUE1}",
                    "{ENTITY2}": "{VALUE2}",
                    ...
                }
            }
        ],
        "entities": ["{ENTITY1}", "{ENTITY2}", ...],
        "language": "en",
        "modeltype": "spacy"
    }

It is generally not recommended using this endpoint for `curl` commands,
as it easily gets chaotic and is fairly long, but the general `curl`
command would be:

    curl -X POST -H "Content-Type: application/json" -d '{YOUR JSON OBJECT}' http://demos.swe.htwk-leipzig.de:40170/retrain

and a working example is:

    curl -X 'POST' \
        'http://demos.swe.htwk-leipzig.de:40170/retrain' \
        -H 'Content-Type: application/json' \
        -d '{
        "testingdata": [
        {
            "text": "I am called Marilyn Monroe.",
            "language": "en",
            "entities": {
                "First_Name": "Marilyn",
                "Last_Name": "Monroe"
            }
            }
        ],
        "trainingdata": [
            {
            "text": "I am called Marilyn Monroe.",
            "language": "en",
            "entities": {
                "First_Name": "Marilyn",
                "Last_Name": "Monroe"
            }
            }
        ],
        "entities": [
            "First_Name",
            "Middle_Name",
            "Last_Name"and this is
    }'

### Health endpoint

To check if the service is active, just run:
<http://demos.swe.htwk-leipzig.de40170/health>

ML Flow Logging
---------------

You can use ML Flow Logging with this service. For information on the
setup and usage of an ML Flow Server, please refer to its
[Documentation](https://www.mlflow.org/docs/latest/tracking.html). ML
Flow Logging is always activated for interactions with the service from
the Qanary interface, triggering the ([NER Logging](#ner-logging)). It
might as well be used for interactions with the
[/retrain](#retrain-endpoint) ([Training Logging](#training-logging))
and the [/api](#api-endpoint) ([NER Logging](#ner-logging)) endpoint by
setting the parameter `MLFLOW_ACTIVATED` to `True`. The parameter is
found in the [inner .env
file](./AutomationService/AutomationServiceBackend/app/.env).

### Training Logging

When starting a training process via the `\retrain`-endpoint with the
`use_ml_logger` parameter set to `True`, the training will be logged
once its concluded. The logs can be found in the `AutoML Model Training`
tab. The logged data contains the attributes:

-   `component_name`: The name of the component that triggered this log

-   `component_type`: The type of the component, in this case always NER

-   `entities`: The entities this trained model could recognize

-   `hardware`: The hardware the model was trained on

-   `language`: The language of the model, specified by the user

-   `model`: The model that was used. SpaCy returns multiple models (the
    last and the best), but the component always takes "model-best",
    which was the best performing.

-   `model_uuid`: The UUID that’s assigned to this training run.

-   `modeltype`: The model type entered with the training options

-   `time`: The time needed to conclude the training

Within the "Artifacts", there are some files logged:

-   `Datasets`: In this directory, text files are stored that contain
    the training and testing data given

-   `config.json`: The configuration used to train the model

-   `model_metrics.json`: This file is the meta.json of the model, it
    contains all kinds of information such as the performance while
    training.

When the training is concluded, the testdata is used to trigger the NER
process and log the results for each given input. This logging happens
within the [NER Logging](#ner-logging) and the UUID will be the same for
the training-logs as well as the NER logs.

### NER Logging

When a POST request is sent to the `/api` endpoint (found in the
`AutoML Model Testing` tab), with the `use_ml_logger` parameter set to
`True`, the NER results will be logged for each of the given input
texts. Files will not be logged as one but each input line by itself.
The logged values are:

-   `input`: The given input text

-   `model_uuid`: The UUID of this call; It will be the same for all
    input texts of the same file and if the process is triggered through
    the training, it will be the same as the training process, too.

-   `runtime`: The time needed for the result for this text.

Within the `Artifacts`, there are two files logged:

-   `predicted_target.json`: The result of the NER

-   `true_target.json`: The expected result, if provided with the input

### Annotation Logging

When a text is entered in the Qanary interface (found in the
`AutoML Component Annotations` tab), the created annotations are logged,
too. There are no additional parameters to be set as this is a
requirement. The logged data is:

-   `input`: The given input text

-   `model_uuid`: The UUID of this call

-   `predicted_target`: The result of the NER, containing the recognized
    entities and their positions within the input

-   `qanary_graph_id`: The graph the annotations was saved to

Please note that the process of logging NER uploads can take up some
time if bigger datasets are provided.

Ready to go Docker Images
=========================

There are Docker images available that have pre-trained models for name
and address recognition - one using a spacy model as a base and one
using no base at all. They can be found in the [Qanary
Dockerhub](https://hub.docker.com/u/qanary), named
`qanary/qanary-component-ner-automl-pretrained-{the model you want}`.
Note that these are built to be run as part of the qanary pipeline. For
example, you could replace the build call in the

-   [The image with a spacy based model for name (first, middle and last
    name) recognition in
    GER](https://hub.docker.com/r/qanary/qanary-component-ner-automl-pretrained-name-spacy-de)

-   [The image with a spacy based model for name (first, middle and last
    name) recognition in
    EN](https://hub.docker.com/r/qanary/qanary-component-ner-automl-pretrained-name-spacy-en)

-   [The image with a bert based model for name (first, middle and last
    name) recognition in
    GER](https://hub.docker.com/r/qanary/qanary-component-ner-automl-pretrained-name-bert-de)

-   [The image with a bert based model for name (first, middle and last
    name) recognition in
    EN](https://hub.docker.com/r/qanary/qanary-component-ner-automl-pretrained-name-bert-en)

-   [The image without a base model for name (first, middle and last
    name) recognition in
    GER](https://hub.docker.com/r/qanary/qanary-component-ner-automl-pretrained-name-nobase-de)

-   [The image without a base model for name (first, middle and last
    name) recognition in
    EN](https://hub.docker.com/r/qanary/qanary-component-ner-automl-pretrained-name-nobase-en)

-   [The image with a spacy based model for address (street, house
    number, postal code and city) recognition in
    GER](https://hub.docker.com/r/qanary/qanary-component-ner-automl-pretrained-address-spacy-de)

-   [The image with a spacy based model for address (street, house
    number, postal code and city) recognition in
    EN](https://hub.docker.com/r/qanary/qanary-component-ner-automl-pretrained-address-spacy-en)

-   [The image with a bert based model for address (street, house
    number, postal code and city) recognition in
    GER](https://hub.docker.com/r/qanary/qanary-component-ner-automl-pretrained-address-bert-de)

-   [The image with a bert based model for address (street, house
    number, postal code and city) recognition in
    EN](https://hub.docker.com/r/qanary/qanary-component-ner-automl-pretrained-address-bert-en)

-   [The image without a base model for address (street, house number,
    postal code and city) recognition in
    GER](https://hub.docker.com/r/qanary/qanary-component-ner-automl-pretrained-address-nobase-de)

-   [The image without a base model for address (street, house number,
    postal code and city) recognition in
    EN](https://hub.docker.com/r/qanary/qanary-component-ner-automl-pretrained-address-nobase-en)
