# Azure ML pipelines

### **Objetivo:**   
Con base a dos modelos de machine learning: Logistic Regression y Decision Tree predecir si una muestra de aguas es o no es potable, utilizando un pipeline desarollado en el SDK de Azure
ML.

### **1. Requerimientos**
- Un espacio de trabajo de Azure Machine Learning.
- Un environment python
- Azure Machine Learning Python SDK v2 -worskspace de python SDK
- La data utilizada es [water_potability_ds.csv](https://github.com/carolina-alp/azure-ml-pipeline-water-potability/blob/main/water_potability_ds.csv), que debe ser cargada mediante `Assets` como un uri_file 

### **2. Procedimiento** 

A continuación se describe brevemente los aspectos mas relevantes del procedimento.

- En el archivo  [orchestrator](https://github.com/carolina-alp/azure-ml-pipeline-water-potability/blob/main/orchestrator.ipynb) se ejecutan la tareas para generar y cargar los archivos necesarios

En primera instancia se cargan las herramientas necesarias desde `azure.ai.ml`

- **2.1 Creación de un environment**   
    Necesario para cargar el componente `fill_eda-component` utilizando:
    ```
    from azure.ai.ml.entities import Environment
    ```
    El environment se denomina `"project-Environment"`, lo anterior se debe a que los curated environments de azure no tienen la dependencia de seaborn. Las caracteristicas del nuevo environment se encuentran en la carpeta [`environment`](https://github.com/carolina-alp/azure-ml-pipeline-water-potability/tree/main/environment).
<br><br>
- **2.2 Definición del entorno**
    Se busca un recurso de computación con la función
    ```
    def get_comput_target.
    ```
    Denominado `cpu-cluster` Si no existe, se crea un nuevo recurso con las especificaciones. Si no existe, se crea un nuevo recurso con las especificaciones:
    - Tipo: amlcompute
    - Tamaño: Standard_D2_v2
    - Tiempo de inactividad antes de la reducción de escala: 180 minutos
    - Número mínimo de instancias: 0
    - Número máximo de instancias: 2
    - Nivel de servicio: Dedicado
<br><br>
- **2.3 Cargar de componentes**

    Los componente se cargan utilizando el load componente mediante los archivos .yml
    ```
    fill_eda_component = load_component(source="./fill_eda-component/fill_eda.yml")
    split_component = load_component(source="./split-component/split.yml")
    train_lr_component = load_component(source="./train_LogisticRegression_component/train_LogisticRegression.yml")
    train_dt_component = load_component(source="./train_DecisionTree_component/train_DecisionTree.yml")
    score_component = load_component(source="./score-component/score.yml")
    eval_component = load_component(source="./eval-component/eval.yml")
    ```
    
    Las tareas a realizar y los archivos de salida de cada componente son:

    - `fill_eda-component`:
        Rellenar los nan values con la media de la variable.<br>Los datos de salida son la data rellenada-limpia (uri_file) y un uri_folder donde se guarda la grafica de pairplot. 
    - `split-component`: 
    Dividir la data rellenada-limpia en dos, data_train y data_test, ambos archivos son salidas son de tipo uri_file.
    - `train_LogisticRegression_component`: Ajustar el modelo con el train data.<br>La salida es un uri_folder que guarda el modelo ajustado en formato pkl 
    - `train_DecisionTree_component`: Ajustar el modelo con el train data.<br>La salida es un uri_folder que guarda el modelo ajustado en formato pkl
    - `score-component`: Predecir la variables con base al test data y a los modelos ajustados
    - `eval-component`: Evaluar los datos predecidos con los datos reales
    <br><br>
- **2.4 Definir pipeline**
    Se define el pipeline utilizando la función utilizando los componente definidos
    ```
    water_potability_prediction(pipeline_input_data)  
    ```
    
   <br>
- **2.5 Guardar archivos**
    Se guardan los datos de salida en una carpeta: pipeline_output
    
    ```
    output = ml_client.jobs.download(name=pipeline_job.name, download_path='./pipeline_output', all=True)

    ```    
    