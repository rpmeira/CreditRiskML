# CreditRiskML  
**End-to-End Machine Learning Project for Credit Risk Prediction**  
✅ Data Analysis | ✅ Predictive Modeling | ✅ MLOps (AWS + Docker)

<br>
<div align="center">  
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">  
  <img src="https://img.shields.io/badge/scikit_learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Scikit-learn">  
  <img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white" alt="TensorFlow">  
  <img src="https://img.shields.io/badge/Amazon_AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white" alt="AWS">  
  <img src="https://img.shields.io/badge/Tableau-E97627?style=for-the-badge&logo=Tableau&logoColor=white" alt="Tableau">  
</div>  

---

<br>

## 📌 Sobre o Projeto *(About the Project)*  
Este projeto tem como objetivo **prever a inadimplência em operações de crédito** utilizando técnicas de *Machine Learning* e práticas modernas de *MLOps*. Inspirado em desafios reais do setor financeiro, ele simula o fluxo completo de desenvolvimento de uma solução preditiva, desde a análise exploratória até o *deploy* em ambiente cloud e monitoramento contínuo.  

### **Objetivos Técnicos**  
1. **Desenvolver modelos preditivos** robustos (*XGBoost*, redes neurais) para classificação binária (inadimplente vs. não inadimplente).  
2. **Implementar práticas de MLOps**:  
   - *Deploy* de modelos em produção usando **Docker** e **AWS EC2/S3**.  
   - Pipeline de CI/CD com **GitHub Actions** para automação de testes e atualizações.  
3. **Garantir escalabilidade e monitoramento**:  
   - Dashboard no **Tableau** para visualização de métricas de desempenho.  
   - Detecção de *data drift* para alertas proativos.  

### **Fases do Projeto**  
| Fase               | Principais Tarefas                                      | Tecnologias-Chave                          |  
|---------------------|--------------------------------------------------------|--------------------------------------------|  
| **MVP (Fase 1)**    | Análise exploratória, modelo baseline (regressão logística), API local com Flask. | Python, Pandas, Scikit-learn, Flask        |  
| **Aprimoramento (Fase 2)** | Engenharia de features avançada, modelos complexos (XGBoost, redes neurais), deploy na AWS. | XGBoost, TensorFlow, Docker, AWS EC2       |  
| **Refinamento (Fase 3)**   | Dashboard interativo, testes automatizados (pytest), cálculo de impacto financeiro. | Tableau, pytest, Matplotlib, Optuna        |  

## 📂 Estrutura do Repositório  
- `fase_1_mvp/`: Código e análise do MVP.  
- `fase_2_aprimoramento/`: Engenharia de features avançada e MLOps.  
- `fase_3_refinamento/`: Dashboards e documentação técnica.  
