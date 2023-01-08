## 블로그 작성글
블로그 링크: [주피터 노트북 서버 만들기](https://seokii.tistory.com/205)  
<br>

## 1. Kubeflow 대시보드 접속
1. kubectl 명령어로 쿠브플로우 대시보드에 접속합니다.
```
kubectl port-forward --address 0.0.0.0 svc/istio-ingressgateway -n istio-system 8080:80
```

2. 대시보드 왼쪽 메뉴에서 Notebooks를 클릭합니다.  
<br>

## 2. Notebook Servers
노트북 서버는 쿠버네티스 위에서 실행되는 주피터 노트북 서버입니다.  
쿠버네티스의 리소스 스케줄링을 통해 사용자는 노트북의 설정을 통해 간단히 노트북을 할당받을 수 있습니다.  

1. NEW NOTEBOOK 버튼 클릭  
2. 알맞은 옵션을 정의합니다.
    - Name : 노트북 서버를 구분할 수 있는 이름
    - Namespace : 현재 로그인한 유저의 계정이 자동 지정됨
    - Image : sklearn, tensorflow, pytorch 등의 파이썬 패키지가 설치된 jupyter lab 이미지를 선택해 사용할 수 있습니다.  
    추가적으로 커스텀 이미지를 만들어 생성할 수 있습니다.
    - CPU/RAM : 노트북이 사용할 cpu와 메모리 할당량을 설정할 수 있습니다. 기본 값은 각각 0.5, 1.0Gi 입니다.
    - GPUs : 노트북에 할당할 GPU 개수를 설정할 수 있습니다.
    - Workspace Volume : 노트북 서버 내에서 필요한 디스크 용량을 설정합니다.
    - Data Volumes : 추가적인 스토리지 자원을 설정할 수 있습니다.
    - Configurations : 별도의 환경변수 혹은 시크릿 값 등을 설정할 수 있습니다.  
  
    다음 명령어로 CPU와 메모리에 대한 사용 가능한 할당량을 확인할 수 있습니다.  
    ```
    kubectl get nodes "-o=custom-columns=NAME:.metadata.name,CPU:.status.allocatable.cpu,MEMORY:.status.allocatable.memory"
    ```
    
  3. LAUNCH 버튼을 클릭해 노트북 서버를 생성합니다.  
  4. Status의 상태가 계속 진행되면서 노트북이 생성되지 않거나,  
    노트북 서버 삭제가 원활하게 이루어지지 않는 경우에는 공식 Docs의 명령어를 통해 로그 등을 확인할 수 있습니다.  
    > 공식 Docs : [notebooks Troubleshooting](https://www.kubeflow.org/docs/components/notebooks/troubleshooting/)  
