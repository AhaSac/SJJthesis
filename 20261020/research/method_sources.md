# 方法与前沿文献核验记录

检索/核验日期：2026-10-20。主选时间范围2016—2026年；以下7条按“离散精度—湍流保真度—可信度—受约束加速”组织。并非文献计量穷尽检索。正文宜选前6条中的3—4条作方法支撑，量子条目仅用于展望，以免挤占泵应用的约3000字篇幅。

编辑压缩建议：根编辑已有Zhang2017高阶离散文献，方法与AI正文约450字时，主用 **Bose2018WMLES、Xiao2019Uncertainty、Kochkov2021MLCFD、Xue2024LBM、Succi2023Quantum** 五篇即可；其中量子若不展开也可只放延伸阅读。后文新增Succi2023为正式同行评议Perspective，可替代Lapworth预印本，核心正文不必同时引用两条量子文献。

## M1 高阶离散：Xu2018Spectral

Hui Xu; Chris D. Cantwell; Carlos Monteserin; Claes Eskilsson; Allan P. Engsig-Karup; Spencer J. Sherwin. **Spectral/hp element methods: Recent developments, applications, and perspectives**. *Journal of Hydrodynamics*, 2018, 30(1):1–22. DOI: **10.1007/s42241-018-0001-1**.

- 出版社原文/开放全文：[Springer](https://link.springer.com/article/10.1007/s42241-018-0001-1)。机构完整书目与BibTeX：[DTU](https://orbit.dtu.dk/en/publications/spectralhp-element-methods-recent-developments-applications-and-p/)。作者预印本：[arXiv:1802.06743](https://arxiv.org/abs/1802.06743)。期刊介绍：[Journal of Hydrodynamics](https://www.jhydrodynamics.com/en/spectral-hp-element-methods-recent-developments-applications/)。
- 支持内容：谱/hp元将有限元几何适应性与高次多项式逼近结合，可通过细化网格h和提高阶次p改善误差；综述涉及去混叠、谱消失黏性及隐式LES。为“高阶离散”与“高保真湍流模型”是不同维度提供来源。
- 限制：关于随p提高的指数收敛有解光滑性等前提；不能写成任意泵内汽蚀/分离流都能指数收敛。原文应用重在转捩和海洋工程，没有证明泵工业全面替代有限体积法。
- 访问层级：出版社OA全文可用，完整书目核验。

## M2 近壁代价与LES：Bose2018WMLES

Sanjeeb T. Bose; George Ilhwan Park. **Wall-Modeled Large-Eddy Simulation for Complex Turbulent Flows**. *Annual Review of Fluid Mechanics*, 2018, 50:535–561. DOI: **10.1146/annurev-fluid-122316-045241**.

- 出版社原文：[Annual Reviews](https://www.annualreviews.org/content/journals/10.1146/annurev-fluid-122316-045241)。
- 支持内容：高雷诺数壁湍流的小尺度使壁分辨LES/DNS成本上升，壁模LES通过近壁建模减少解析负担；分离、转捩等复杂工况需要审查壁模假设。适用于解释为何工程泵需要RANS/URANS—混合RANS/LES—LES的分级策略。
- 限制：不可将LES标签直接当作精度保证；旋转、曲率、强逆压梯度、间隙流下壁模适用性要重新验证。未提供通用“LES比URANS精确多少”的泵误差数字。
- 访问层级：出版社书目、摘要、索引全文片段及结论已核验；页面全文异步加载，未逐页全文精读。

## M3 模型不确定度：Xiao2019Uncertainty

Heng Xiao; Paola Cinnella. **Quantification of model uncertainty in RANS simulations: A review**. *Progress in Aerospace Sciences*, 2019, 108:1–31. DOI: **10.1016/j.paerosci.2018.10.001**.

- 出版社：[ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0376042118300952)。机构作者稿全文：[Arts et Métiers/SAM](https://sam.ensam.eu/bitstream/10985/15519/3/DynFluid_PAS_2019_XIAO.pdf)。预印本：[arXiv:1806.10434](https://arxiv.org/abs/1806.10434)。
- 支持内容：区分湍流模型参数误差与结构误差，评述无数据不确定度传播和数据驱动统计推断；RANS的成本和稳健性仍有工程价值。用于说明网格无关性不能消除湍流闭合误差，试验验证应与数值收敛分开。
- 限制：主要针对RANS模型不确定度，不是ASME验证标准；不可将其当作给出了泵性能合格误差阈值。没有普适“相对误差小于3%即高精度”结论。
- 访问层级：出版社摘要/结论及机构PDF前页内容已核验，机构全文公开可用。

## M4 数据与物理约束：Duraisamy2019Data

Karthik Duraisamy; Gianluca Iaccarino; Heng Xiao. **Turbulence Modeling in the Age of Data**. *Annual Review of Fluid Mechanics*, 2019, 51:357–377. DOI: **10.1146/annurev-fluid-010518-040547**.

- 出版社：[Annual Reviews](https://www.annualreviews.org/content/journals/10.1146/annurev-fluid-010518-040547)。作者预印本：[arXiv:1804.00183](https://arxiv.org/abs/1804.00183)。
- 支持内容：将试验与DNS数据用于闭合模型的系统校准和偏差估计，强调物理约束及湍流知识。AI可以服务于减少模型误差，不能仅以推理速度作为“高精度”的证据。
- 限制：综述不等同于已经解决分布外泵工况；训练数据范围、物理可实现性、与求解器耦合稳定性均需评估。它讨论的AI并不限于LBM。
- 访问层级：出版社完整书目、摘要及索引全文片段已核验；作者预印本开放。

## M5 AI加速算例及外推边界：Kochkov2021MLCFD

Dmitrii Kochkov; Jamie A. Smith; Ayya Alieva; Qing Wang; Michael P. Brenner; Stephan Hoyer. **Machine learning–accelerated computational fluid dynamics**. *Proceedings of the National Academy of Sciences*, 2021, 118(21):e2101784118. DOI: **10.1073/pnas.2101784118**.

- 正式DOI：[PNAS](https://doi.org/10.1073/pnas.2101784118)。原论文存档：[PMC8166023](https://pmc.ncbi.nlm.nih.gov/articles/PMC8166023/)。核验摘要与作者：[PubMed](https://pubmed.ncbi.nlm.nih.gov/34006645/)。作者预印本：[arXiv:2102.01010](https://arxiv.org/abs/2102.01010)。作者代码：[Google jax-cfd](https://github.com/google/jax-cfd)。
- 支持内容：用端到端学习改进二维湍流求解器内部近似；在所测算例下，粗网格模型达到各方向8—10倍更细基线网格的精度，报告约40—80倍计算加速，并考察长期稳定性。
- 限制：二维湍流是限定条件；作者机构为Google/Harvard，不能称英国LBM论文，也不可将40—80倍写成三维旋转汽蚀泵或声学计算已经实现的加速。
- 访问层级：PubMed正式元数据和完整摘要已核验，PMC/预印本全文有公开入口；PMC本次打开遇验证码，未据其宣称逐页精读。

## M6 与“英国学者AI+LBM”记忆接近：Xue2024LBM

Xiao Xue; Shuo Wang; Hua-Dong Yao; Lars Davidson; Peter V. Coveney. **Physics informed data-driven near-wall modelling for lattice Boltzmann simulation of high Reynolds number turbulent flows**. *Communications Physics*, 2024, 7:338. DOI: **10.1038/s42005-024-01832-1**. 正式发表：2024-10-15。

- 出版社OA原文：[Nature/Communications Physics](https://www.nature.com/articles/s42005-024-01832-1)。机构正式PDF：[Eindhoven](https://research.tue.nl/files/349848181/s42005-024-01832-1.pdf)。作者稿：[arXiv:2402.08037](https://arxiv.org/abs/2402.08037)。代码：[UCL-CCS/PINN-WM-LBM](https://github.com/UCL-CCS/PINN-WM-LBM)。
- 支持内容：UCL参与团队把物理约束神经网络壁模接入LBM近壁LES，以IDDES槽道流数据训练；训练Re_tau=5200，针对近壁稀疏数据开展评估。它是兼顾成本和保真度的“辅助壁模”路径。
- 关键限制：DNS对比至Re_tau=5200；Re_tau=10^6部分仅与对数壁律比较，原文明确该尺度没有DNS数据。不能说已由DNS验证到百万摩擦雷诺数，更不能说已在泵内分离、旋转、汽蚀或噪声上验证。它与用户记忆接近，但没有足够信息认定用户想到的就是此人/此文。
- 访问层级：出版社索引摘要/结论、机构正式PDF前页、补充材料作者机构核验；OA全文可用。结论关键区分由出版社检索索引直接支持。

## M7 量子计算的真实成熟度：Lapworth2022Hybrid

Leigh Lapworth. **A Hybrid Quantum-Classical CFD Methodology with Benchmark HHL Solutions**. *arXiv preprint*, 2022, arXiv:2206.00419. DOI: **10.48550/arXiv.2206.00419**.

- 作者原始预印本：[arXiv:2206.00419](https://arxiv.org/abs/2206.00419)。
- 支持内容：Rolls-Royce英国团队将SIMPLE外层迭代与HHL线性方程求解结合，在二维顶盖方腔研究精度与经典预处理代价。
- 关键限制：量子部分使用状态矢量模拟器；完整非线性混合算例只有5×5、9×9小网格。较大至65×65网格是矩阵/分解研究，不能混写成完整量子CFD。没有证明量子硬件对工程泵优于经典计算；公开记录未列正式期刊引用，故必须保留预印本身份。
- 访问层级：arXiv原始元数据及完整摘要核验，PDF开放可用。

## 可直接采用的BibTeX草稿

此处只提供核验书目数据，主编辑者可纳入references.bib；本角色没有编辑项目bib文件。

```bibtex
@article{Xu2018Spectral,
  author = {Xu, Hui and Cantwell, Chris D. and Monteserin, Carlos and Eskilsson, Claes and Engsig-Karup, Allan P. and Sherwin, Spencer J.},
  title = {Spectral/hp element methods: Recent developments, applications, and perspectives},
  journal = {Journal of Hydrodynamics}, year = {2018}, volume = {30}, number = {1}, pages = {1--22},
  doi = {10.1007/s42241-018-0001-1}, url = {https://link.springer.com/article/10.1007/s42241-018-0001-1}
}
@article{Bose2018WMLES,
  author = {Bose, Sanjeeb T. and Park, George Ilhwan},
  title = {Wall-Modeled Large-Eddy Simulation for Complex Turbulent Flows},
  journal = {Annual Review of Fluid Mechanics}, year = {2018}, volume = {50}, pages = {535--561},
  doi = {10.1146/annurev-fluid-122316-045241}, url = {https://doi.org/10.1146/annurev-fluid-122316-045241}
}
@article{Xiao2019Uncertainty,
  author = {Xiao, Heng and Cinnella, Paola},
  title = {Quantification of model uncertainty in {RANS} simulations: A review},
  journal = {Progress in Aerospace Sciences}, year = {2019}, volume = {108}, pages = {1--31},
  doi = {10.1016/j.paerosci.2018.10.001}, url = {https://doi.org/10.1016/j.paerosci.2018.10.001}
}
@article{Duraisamy2019Data,
  author = {Duraisamy, Karthik and Iaccarino, Gianluca and Xiao, Heng},
  title = {Turbulence Modeling in the Age of Data},
  journal = {Annual Review of Fluid Mechanics}, year = {2019}, volume = {51}, pages = {357--377},
  doi = {10.1146/annurev-fluid-010518-040547}, url = {https://doi.org/10.1146/annurev-fluid-010518-040547}
}
@article{Kochkov2021MLCFD,
  author = {Kochkov, Dmitrii and Smith, Jamie A. and Alieva, Ayya and Wang, Qing and Brenner, Michael P. and Hoyer, Stephan},
  title = {Machine learning-accelerated computational fluid dynamics},
  journal = {Proceedings of the National Academy of Sciences}, year = {2021}, volume = {118}, number = {21},
  pages = {e2101784118}, doi = {10.1073/pnas.2101784118}, url = {https://pmc.ncbi.nlm.nih.gov/articles/PMC8166023/}
}
@article{Xue2024LBM,
  author = {Xue, Xiao and Wang, Shuo and Yao, Hua-Dong and Davidson, Lars and Coveney, Peter V.},
  title = {Physics informed data-driven near-wall modelling for lattice {Boltzmann} simulation of high {Reynolds} number turbulent flows},
  journal = {Communications Physics}, year = {2024}, volume = {7}, pages = {338},
  doi = {10.1038/s42005-024-01832-1}, url = {https://www.nature.com/articles/s42005-024-01832-1}
}
@online{Lapworth2022Hybrid,
  author = {Lapworth, Leigh},
  title = {A Hybrid Quantum-Classical {CFD} Methodology with Benchmark {HHL} Solutions},
  year = {2022}, eprint = {2206.00419}, eprinttype = {arxiv}, eprintclass = {quant-ph},
  doi = {10.48550/arXiv.2206.00419}, url = {https://arxiv.org/abs/2206.00419},
  note = {预印本}
}
```

## 泵综述写法建议（为编辑判断，不冒充文献结论）

建议把“高精度”限定为对指定工程量的可验证误差控制：扬程和扭矩对应积分平均量；激振力、叶频及谐波对应非定常载荷；叶缘与舌部湍流、间隙涡和空泡结构可影响宽带脉动及声源。由此自然引入空间、时间和统计收敛以及声传播/结构响应的额外误差链。不能把“叶缘流速”单独立为全行业最高精度指标，也不能把叶频压力峰值预测好当作宽带噪声已经准确。

AI/LBM建议占正文一个段落；量子计算最多一两句或放补充阅读。按这些来源，较稳妥的结论是“物理约束学习有望降低部分近壁与粗网格计算成本，但精度判据和工况外验证仍决定工程采用”。

## 附：国内高阶离散备选（不纳入上述7条核心）

H. X. Zhang; L. P. Zhang; S. H. Zhang; Q. S. Li. **Some recent progress of high-order methods on structured and unstructured grids in CARDC**. *Computers & Fluids*, 2017, 154:371–389. DOI [10.1016/j.compfluid.2016.10.006](https://doi.org/10.1016/j.compfluid.2016.10.006)。出版社摘要及引言可被检索：[ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0045793016303073)。国内期刊对该文作者缩写/页码的引用核对：[空气动力学学报](https://kqdlxxb.xml-journal.net/cn/article/id/10f33a75-05bf-4662-8917-d108ec4402c5)。主题为CARDC结构/非结构网格高阶有限差分、DG/FV混合，支持讨论低耗散离散对多尺度涡流/声学的意义。未拿到该文PDF或出版社完整作者展示，因此仅作备选，建议如采用再核对正式BibTeX导出；不要把第三方数据库多重机构误识为多名作者。

## 新增：正式期刊量子综述，可替代M7预印本

Sauro Succi; Wael Itani; Katepalli Sreenivasan; René Steijl. **Quantum computing for fluids: Where do we stand?** *EPL (Europhysics Letters)*, 2023, 144(1):10001. DOI **10.1209/0295-5075/acfdc7**. 发表2023-10-16。

- [原出版社DOI](https://doi.org/10.1209/0295-5075/acfdc7)；[现出版社可读全文](https://academic.oup.com/epl/article/144/1/acfdc7/8765615)；[作者全文预印本](https://arxiv.org/html/2307.05157v1)。原IOP书目以文章号10001给出，迁移后Oxford页面以DOI后缀acfdc7为电子定位符，两者不是两篇文献。
- 支持内容：正式Perspective综述量子CFD、混合方法、Carleman-LBM等路径；明确非线性、耗散、量子读出和状态初始化是障碍，结论认为实用化仍需量子技术尤其纠错进展。英国Glasgow的Steijl为共同作者，可作为用户记忆中英国学者量子LBM的真实近邻来源。
- 限制：它不提供工业泵实机加速证据，不能根据表示流场需要多少量子比特的理论容量估计推导出现有硬件已经足以高精度计算工程泵。
- 访问层级：出版社完整HTML全文已核验，重点读了Challenges、Carleman lattice Boltzmann method及Conclusions；作者名全拼由arXiv原始作者记录核验。

```bibtex
@article{Succi2023Quantum,
  author = {Succi, Sauro and Itani, Wael and Sreenivasan, Katepalli and Steijl, Ren{\'e}},
  title = {Quantum computing for fluids: Where do we stand?},
  journal = {EPL (Europhysics Letters)}, year = {2023}, volume = {144}, number = {1}, pages = {10001},
  doi = {10.1209/0295-5075/acfdc7}, url = {https://doi.org/10.1209/0295-5075/acfdc7}
}
```
