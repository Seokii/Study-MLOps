# Kubeflow Katib
쿠브플로우 카티브에 대한 설명입니다.  
블로그 링크: https://seokii.tistory.com/208  

## Katib Documentation
쿠브플로우 카티브 공식 문서 사이트입니다.  
Docs: https://www.kubeflow.org/docs/components/katib/  
공식 문서를 통해 다음 내용을 확인할 수 있습니다.  
- Introduction to Katib
- Getting Started with Katib
- Running an Experiment
- Resuming an Experiment
- Overview of Trial Templates
- Using Early Stopping
- Katib Configuration Overview
- Environment Variables for Katib Components
&nbsp;<br>

## Introduction Katib
공식 문서에 따르면 카티브는 AutoML을 위한 쿠버네티스 프로젝트입니다.  
카티브는 **하이퍼 파라미터 튜닝(Hyperparameter Tuning)** 과 **신경망 아키텍처 탐색(Neural Architecture Search, NAS)** 을 지원합니다.  
카티브는 Tensorflow, Pytorch, MXNet, XGBoost 등 다양한 머신러닝 프레임워크를 제공하고 있습니다.  
Katib는 아랍어로 '비서'라는 뜻을 가지고 있습니다.  

#### 하이퍼파라미터 튜닝
하이퍼 파라미터는 모델 학습 과정에서 사용자가 지정하는 변수들을 의미합니다.  
몇 가지의 예시는 다음과 같습니다.  
- Learning Rate
- Dropout Rate
- Cost Function
- Nueral Net의 레이어 수

이 값들을 조정하며 모델의 성능을 개선할 수 있는데 이 과정을 **하이퍼파라미터 최적화** 라고 합니다.  
카티브는 이러한 튜닝 과정을 자동화 해주는 기능을 제공하고 있습니다.  

#### 신경망 아키텍처 탐색
신경망 아키텍처 탐색(NAS)은 AutoML의 하나로서, **인공 신경망 설계를 자동화하는 기술** 입니다.  
카티브의 NAS는 강화 학습을 사용하고 있습니다.  
&nbsp;<br>

카티브를 사용하기 위해서는 다음과 같은 알아야 할 **4가지의 주요 개념** 이 있습니다.
- Experiment (실험)
- Suggestion (제안)
- Trial (시도)
- Worker Job (작업)

#### Experiment
Experiment는 하이퍼 파라미터 값들을 찾는 탐색 작업이며, 하나의 최적화 실행 단위입니다.  
Experiment에는 다음과 같은 구성 요소가 있습니다.  
- Objective(목표) : 사용할 평가지표와 방향(지표에 따라 높일지 낮힐지에 대한 결정)
- Search space(탐색 범위) : 튜닝 과정에서 사용할 모든 하이퍼 파라미터 값과 범위에 대한 제약 조건
- Search algorithm(탐색 알고리즘) : 최적값을 탐색하기 위한 알고리즘

#### Suggestion
탐색 알고리즘이 제안한 하이퍼 파라미터 값들의 집합입니다.  
하나의 Experiment 당 하나의 Suggestion이 생성되며,  
Experiment에서 설정된 파라미터와 탐색 알고리즘이 만들어낸 값을 각 Trial에 제공합니다.  

#### Trial
최적화 과정의 반복 단위를 뜻합니다.  
Experiment의 Trial count 수만큼 Trial이 생성되며,  
하나의 Trial이 종료되면 그 다음 Trial이 생성됩니다.  
하나의 Trial은 하나의 Worker job에서 실행됩니다.  
정리하자면, 각 Experiment 는 여러 번의 Trial을 수행하고  
Experiment는 목표나 설정한 최대 시도 횟수에 도달 할 때까지 Trial 을 계속 실행합니다.  

#### Worker Job
Worker Job은 Trial을 평가하고 목표 값을 계산하는 프로세스입니다.  
제안된 하이퍼 파라미터 값들을 받아 실제로 모델을 학습합니다.  
단일 실행인 쿠버네티스 Job과 분산 실행인 TFJob, PyTorchJob 기능을 제공합니다.  
