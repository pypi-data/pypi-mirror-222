# Returns the MD5 sum of the original data as the response.
# pylint: disable=unused-variable
MD5 = """
apiVersion: v1
kind: Pod
metadata:
  name: transformer-md5
  annotations:
    # Values it can take ["hpull://","hrev://","hpush://"]
    communication_type: "{communication_type}://"
    wait_timeout: 5m
spec:
  containers:
    - name: server
      image: aistorage/transformer_md5:latest
      imagePullPolicy: Always
      ports:
        - name: default
          containerPort: 80
      command: ['/code/server.py', '--listen', '0.0.0.0', '--port', '80']
      readinessProbe:
        httpGet:
          path: /health
          port: default
"""

# Returns "Hello World!" on any request.
# pylint: disable=unused-variable
HELLO_WORLD = """
apiVersion: v1
kind: Pod
metadata:
  name: transformer-hello-world
  annotations:
    # Values it can take ["hpull://","hrev://","hpush://"]
    communication_type: "{communication_type}://"
    wait_timeout: 5m
spec:
  containers:
    - name: server
      image: aistorage/transformer_hello_world:latest
      imagePullPolicy: Always
      ports:
        - name: default
          containerPort: 80
      command: ['/code/server.py', '--listen', '0.0.0.0', '--port', '80']
      readinessProbe:
        httpGet:
          path: /health
          port: default
"""

# Returns the original data, with an MD5 sum in the response headers.
# pylint: disable=unused-variable
GO_ECHO = """
apiVersion: v1
kind: Pod
metadata:
  name: echo-go
  annotations:
    # Values it can take ["hpull://","hrev://","hpush://"]
    communication_type: "{communication_type}://"
    wait_timeout: 5m
spec:
  containers:
    - name: server
      image: aistorage/transformer_echo_go:latest
      imagePullPolicy: Always
      ports:
        - name: default
          containerPort: 80
      command: ['./echo', '-l', '0.0.0.0', '-p', '80']
      readinessProbe:
        httpGet:
          path: /health
          port: default
"""

# Returns the original data, with an MD5 sum in the response headers.
# pylint: disable=unused-variable
ECHO = """
apiVersion: v1
kind: Pod
metadata:
  name: transformer-echo
  annotations:
    # Values it can take ["hpull://","hrev://","hpush://"]
    communication_type: "{communication_type}://"
    wait_timeout: 5m
spec:
  containers:
    - name: server
      image: aistorage/transformer_echo:latest
      imagePullPolicy: Always
      ports:
        - name: default
          containerPort: 80
      command: ['/code/server.py', '--listen', '0.0.0.0', '--port', '80']
      readinessProbe:
        httpGet:
          path: /health
          port: default
"""

# Returns the transformed TensorFlow compatible data for the input TAR files. For
# more information on command options, visit 
# https://github.com/NVIDIA/ais-etl/blob/master/transformers/tar2tf/README.md.
# pylint: disable=unused-variable
TAR2TF = """
apiVersion: v1
kind: Pod
metadata:
  name: tar2tf
  annotations:
    # Values it can take ["hpull://","hrev://","hpush://"]
    communication_type: "{communication_type}://"
    wait_timeout: 5m
spec:
  containers:
    - name: server
      image: aistorage/transformer_tar2tf:latest
      imagePullPolicy: Always
      ports:
        - name: default
          containerPort: 80
      # To enable conversion e.g.
      command: ['./tar2tf', '-l', '0.0.0.0', '-p', '80', '{arg}', '{val}']
      readinessProbe:
        httpGet:
          path: /health
          port: default
"""

# Returns the compressed/decompressed file. For more information on command options, visit
# https://github.com/NVIDIA/ais-etl/blob/master/transformers/compress/README.md.
# pylint: disable=unused-variable
COMPRESS = """
apiVersion: v1
kind: Pod
metadata:
  name: transformer-compress
  annotations:
    # Values `communication_type` can take are ["hpull://", "hrev://", "hpush://", "io://"].
    # Visit https://github.com/NVIDIA/aistore/blob/master/docs/etl.md#communication-mechanisms 
    # for more details.
    communication_type: "{communication_type}://"
    wait_timeout: 5m
spec:
  containers:
    - name: server
      image: aistorage/transformer_compress:latest
      imagePullPolicy: Always
      ports:
        - name: default
          containerPort: 80
      command: ['/code/server.py', '--listen', '0.0.0.0', '--port', '80', '{arg1}', '{val1}', '{arg2}', '{val2}']
      readinessProbe:
        httpGet:
          path: /health
          port: default
"""

# pylint: disable=unused-variable
KERAS_TRANSFORMER = """
apiVersion: v1
kind: Pod
metadata:
  name: transformer-compress
  annotations:
    communication_type: "{communication_type}://"
    wait_timeout: 5m
spec:
  containers:
    - name: server
      image: aistorage/transformer_keras:latest
      imagePullPolicy: Always
      ports:
        - name: default
          containerPort: 80
      command: ['/code/server.py', '--listen', '0.0.0.0', '--port', '80']
      env:
        - name: FORMAT
          value: "{format}"
        - name: TRANSFORM
          value: '{transform}'
      readinessProbe:
        httpGet:
          path: /health
          port: default
"""
