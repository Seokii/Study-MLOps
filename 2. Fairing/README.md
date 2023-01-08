# Kubeflow Fairing
쿠브플로우 페어링에 대한 설명입니다.  
블로그 링크: [https://seokii.tistory.com/206](https://seokii.tistory.com/206)

## Faring Documentation
쿠브플로우 페어링 공식 문서 사이트입니다.  
Docs: https://www.kubeflow.org/docs/external-add-ons/fairing/  
<br>
공식 문서를 통해 다음 내용을 확인할 수 있습니디.
- Overview of Kubeflow Fairing
- Install Kubeflow Fairing
- Configure Kubeflow Fairing
- Fairing on Azure
- Fairing on GCP
- Tutorials
- Reference

## Faring 소개
페어링(Fairing)은 쿠브플로우가 설치된 환경에서 ML 모델의 학습과 배포를 도와주는 파이썬 패키지입니다.  
공식 문서에서는 페어링에 대해 다음과 같이 설명합니다.
> 쿠브플로 페어링은 쿠브플로에서 ML 모델을 쉽게 교육하고 배포할 수 있는 파이썬 패키지입니다.  
쿠브플로 페어링은 다른 플랫폼에서 훈련하거나 배포할 수 있도록 확장될 수도 있습니다.  
현재 쿠브플로 페어링은 구글 AI 플랫폼에서 훈련할 수 있도록 확장되었습니다.

<br/>
또한, 쿠브플로 페어링 프로젝트의 목표는 다음과 같습니다.
- 쉬운 ML 모델 훈련 작업 패키지화 : 작성한 모델 학습 코드를 도커 이미지화
- 하이브리드 클라우드 환경에서의 쉬운 학습 : 고급 API를 제공해 기본 인프라에 대한 지식이 필요 없음
- 쉬운 배포 : 학습된 모델을 배치하는 과정 간소화
<br/>
쿠브플로우 페어링에는 다음과 같은 중요한 3가지의 개념이 있습니다.
- Preprocessor(전처리기)
- Builder(빌더)
- Deployer(배포)



