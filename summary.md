# IP cores for Hardware Acceleration of Decision Tree Ensemble Classifiers
## keywords
* **ensemble classifier** : 集成分類器
 
  與之相對應的是single classifier，EC可以由多個SC拼湊而成
  EC比SC有更高的準確度和抗性，代價是需要更多能量維持運作
* **Decision Tree(DT)** : 決策樹

  可分為*axis-parallel*、*oblique*、*non-linear*三種，可以參照本篇的註[25]
  > [25]Implementing Decision Trees in Hardware, J.R. Struharik, 2011

  是一種適合用在硬體的機器學習架構，此外，硬體算法會比軟體算法要快

## summary
* ensemble classifier is composed of two parts: **ensemble evaluator module(EM)** and **combiner module(CM)**
* EM的架構又可分為4種，由慢到快分別為SN、SN2、SP、SP2
* CM像是投票系統，可以依照投票要求來設定給答案的門檻(threshold):let there's N members of ensemble
  * simple majority(大於一半)：floor(N/2)
  * plurality(最多票的):0
  * unanimous(全數通過):N-1
  * weighted sum(加權):要多權重、乘法器、加法器選擇
