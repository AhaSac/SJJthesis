# 泵高精度数值模拟：核验文献与证据边界

核验日期：2026-10-20。检索窗口为2016—2026年，以下可用论文集中于2018—2022年。只将论文出版社、期刊或作者机构页面作为事实依据。部分出版商限制全文访问，因此明确标注摘要/片段级阅读；没有从摘要补造网格数量、模型参数、误差或声学实验。以下不是系统综述的穷尽检索。

## 适合3000字课程综述的主线

从“平均性能是否算对”写到“非定常机制是否解析”，再写“空化和噪声能否可信预测”：稳态扬程/效率 → 分离、尾迹和动静干涉 → 压力脉动/激振力 → 叶顶泄漏涡空化及声振耦合。优先展开P1、P2、P3、P4、P5；P6—P8提供声学边界、工业尺寸及设计应用补充。

“叶缘流速是泵仿真中精度要求最高的量、目的就是降噪”不宜作为定论。叶顶间隙、尾缘和隔舌是重要区域，但准确度取决于目标量：平均扬程与扭矩、脉动幅值和相位、宽带声谱、空化初生/溃灭分别需要不同的分辨率及物理模型。壁面非定常压力、气核条件和结构传声也不能由一个局部速度量替代。不能仅以扬程吻合证明局部涡结构、压力谱和噪声均已验证。

## P1 Kye等：整泵LES揭示偏工况流动损失

- 建议BibTeX键：`Kye2018VoluteLES`。
- 完整作者：Beomjun Kye; Keuntae Park; Haecheon Choi; Myungsung Lee; Joo-Han Kim。
- 题目：Flow characteristics in a volute-type centrifugal pump using large eddy simulation。
- 刊物与年份：International Journal of Heat and Fluid Flow, 2018, 72: 52–60。
- DOI：`10.1016/j.ijheatfluidflow.2018.04.016`。
- [出版社原文页](https://www.sciencedirect.com/science/article/pii/S0142727X17311797)；[摘要页](https://www.sciencedirect.com/science/article/abs/pii/S0142727X17311797)。
- 阅读层级：出版社摘要、方法与结论片段，未取得完整PDF。
- 对象与方法：蜗壳式离心泵，同时考虑叶轮与蜗壳；设计和偏工况；LES使用dynamic global亚格子模型与非惯性系浸入边界。
- 可用结论：偏工况压力面回流和分离增强，尾缘脱落涡与后续叶片涡及径向间隙泄漏发生强相互作用；叶轮—蜗壳干涉与上下腔泄漏均参与非定常损失。
- 验证范围：当前可见片段没有充分展示实验验证细节，不填写误差。
- 不能推出：LES必然比所有RANS更准确；网格加密可以自动替代验证；某一泵的最优几何适用于所有泵。

## P2 Posa：区分导叶入射角与动静径向间距

- 建议BibTeX键：`Posa2021DiffuserAngle`。
- 完整作者：Antonio Posa。
- 题目：LES study on the influence of the diffuser inlet angle of a centrifugal pump on pressure fluctuations。
- 刊物与年份：International Journal of Heat and Fluid Flow, 2021, 89: 108804。
- DOI：`10.1016/j.ijheatfluidflow.2021.108804`。
- [出版社原文页](https://www.sciencedirect.com/science/article/abs/pii/S0142727X21000345)；[CNR作者机构记录](https://iris.cnr.it/handle/20.500.14243/517057)。
- 阅读层级：出版社摘要、导言和结论信息，机构记录摘要；未取得完整PDF。
- 对象与方法：离心泵三种扩压器几何，设计与低流量工况，LES/浸入边界；比较绕前缘旋转导叶与此前绕中弧线旋转导叶的方案。
- 可用结论：低流量时改善导叶进口入射可改善性能与流动均匀性；比较显示叶轮出口到导叶前缘的径向间距对压力脉动的影响比入射角更深。
- 验证范围：论文致谢说明获得Boccazzi和Miorini实验数据，当前可见材料不足以报告逐项验证误差。
- 不能推出：增大间距永远最优；压力脉动降低已证明整机辐射噪声等幅下降。

## P3 Li等：DDES追踪尾迹、导叶与隔舌干涉

- 建议BibTeX键：`Li2022VorticalDDES`。
- 完整作者：Delin Li; Ning Zhang; Junxian Jiang; Bo Gao; Anthony Akurugo Alubokin; Wenjie Zhou; Junlin Shi。
- 题目：Numerical investigation on the unsteady vortical structure and pressure pulsations of a centrifugal pump with the vaned diffuser。
- 刊物与年份：International Journal of Heat and Fluid Flow, 2022, 98: 109050。
- DOI：`10.1016/j.ijheatfluidflow.2022.109050`。
- [出版社原文页](https://www.sciencedirect.com/science/article/abs/pii/S0142727X22001187)。
- 阅读层级：出版社摘要与highlights；未取得完整PDF。
- 对象与方法：带导叶离心泵额定工况，结构网格与DDES；考察涡结构及叶频压力幅值。
- 可用结论：涡量薄层与导叶相互作用使吸力面附近压力脉动增强，压力脉动从导叶前缘向尾缘衰减；导叶尾缘交替脱涡形成涡街，大尺度涡再与蜗舌发生干涉。
- 验证范围：当前摘要未提供实验验证项目与误差，不补写。
- 不能推出：研究已直接计算噪声；“捕获涡街”本身等于宽带压力谱已达到实验精度。

## P4 程怀玉等：空化精度受到气核与涡耦合控制

- 建议BibTeX键：`Cheng2021TLVCavitation`。
- 完整作者：程怀玉; 季斌; 龙新平; 槐文信。
- 题目：空化对叶顶间隙泄漏涡演变特性及特征参数影响的大涡模拟研究。
- 刊物与年份：力学学报, 2021, 53(5): 1268–1287。
- DOI：`10.6052/0459-1879-20-415`。
- [期刊原文页](https://pubs.cstam.org.cn/article/doi/10.6052/0459-1879-20-415)。
- 阅读层级：期刊中英文摘要和元数据；HTML全文未实际加载。
- 对象与方法：NACA0009水翼叶顶间隙，而非整台泵；LES与考虑气核效应的欧拉—拉格朗日空化模型。
- 可用结论：空化后的泄漏涡强度主要受片空化演变影响；较小间隙对应更强的片空化不稳定性及涡强度准周期波动；空化会改变涡核气核分布、涡半径与切向速度结构。
- 验证范围：摘要明确报告数值与实验吻合较好，但不提供误差数值。
- 不能推出：结论已在整泵工况验证；增大间隙改善空化就一定提高泵效率；该文直接验证空化噪声。

## P5 郎涛等：从非定常壁压转入声学计算

- 建议BibTeX键：`Lang2022SingleBladeNoise`。
- 完整作者：郎涛; 金力成; 刘玉涛; 陈刻强; 徐恩翔。
- 题目：单叶片离心泵水动力噪声特性数值分析。
- 刊物与年份：排灌机械工程学报, 2022, 40(6): 541–548。
- DOI：`10.3969/j.issn.1674-8530.20.0358`。
- [期刊原文页](https://zzs.ujs.edu.cn/pgjxgcxb/CN/10.3969/j.issn.1674-8530.20.0358)；[含摘要的当期目录](https://zzs.ujs.edu.cn/pgjxgcxb/CN/Y2022/V40/I6)。
- 阅读层级：期刊目录的完整摘要及文章页元数据；文章页摘要模板未加载，未读取PDF。
- 对象与方法：单叶片离心泵，不同流量；SST k–ω非定常计算与CFD/CA、FW-H声类比。
- 可用结论：压力脉动与内场噪声能量集中于低频、叶频及相应谐频；流量变化导致分离和二次流变化，低频谐频噪声随之变化。
- 验证范围：所读摘要未给声压实验核验，不能写“声学结果已由实验充分验证”。
- 不能推出：该文使用LES；内部水动力噪声等同于泵外空气辐射噪声。正文中可用它说明高精度研究还必须补足声学传播环节。

## P6 He与Shao：气液两相与声振耦合

- 建议BibTeX键：`He2021TwoPhaseNoise`。
- 完整作者：Aixia He; Chunlei Shao。
- 题目：Study on the induced noise of gas–liquid two-phase flow in a centrifugal pump。
- 刊物与年份：Applied Acoustics, 2021, 176: 107892。
- DOI：`10.1016/j.apacoust.2020.107892`。
- [出版社原文页](https://www.sciencedirect.com/science/article/pii/S0003682X20309968)。
- 阅读层级：摘要和方法、实验、结论片段，未取得完整PDF。
- 对象与方法：IS 80-50-250离心泵，不同入口含气率；CFD流场、Virtual.lab声振耦合，考虑蜗壳振动模态。
- 可用结论：该案例的气体引入未改变主频，但含气率增加会恶化流动稳定性和性能并提高流致噪声；壁面压力脉动是其辐射噪声的重要来源。
- 验证范围：有两相流试验，片段显示在低转速验证扬程，且含气率增加时误差增大；结论片段提到压力脉动验证。未看到完整辐射声实验验证，避免声称有。
- 不能推出：气液两相输运等同于蒸汽空化；只靠局部叶缘速度即可确定外场噪声。

## P7 Cui等：工业尺寸多级泵LES与水力激振力

- 建议BibTeX键：`Cui2022ExcitingForces`。
- 完整作者：Baoling Cui; Yingbin Zhang; Yakun Huang; Zuchao Zhu。
- 题目：Analysis of unsteady flow and fluid exciting forces of multistage centrifugal pump based on actual size。
- 刊物与年份：Proceedings of the Institution of Mechanical Engineers, Part A: Journal of Power and Energy, 2022, 236(1): 21–32。在线首发为2021-06-09；以卷期年2022编入BibTeX。
- DOI：`10.1177/09576509211023222`。
- [出版社原文页](https://journals.sagepub.com/doi/10.1177/09576509211023222)。
- 阅读层级：出版社摘要、元数据和作者表；全文受限。
- 对象与方法：实际尺寸多级离心泵，LES，研究级间流场、轴向力与径向力。
- 可用结论：不同级的进口速度分布与各级扬程差异相关；背靠背叶轮与对称双隔舌可降低相应流体力，是高保真结果转向结构布局设计的例子。
- 验证范围：摘要明确以外特性试验核验数值方法；并给出设计点LES与雷诺时均模型的性能误差0.36%与1.14%。这只能作为该案例、该量的比较，不能将其改为激振力或声压误差。
- 不能推出：水力激振力已由动态测力试验独立验证；LES对所有目标量都只存在0.36%误差。

## P8 Ren等：PIV核验、局部流动诊断与叶轮改型

- 建议BibTeX键：`Ren2019SeparationIDDES`。
- 完整作者：Yun Ren; Zuchao Zhu; Denghao Wu; Xiaojun Li; Lanfang Jiang。
- 题目：Investigation of flow separation in a centrifugal pump impeller based on improved delayed detached eddy simulation method。
- 刊物与年份：Advances in Mechanical Engineering, 2019, 11(12)。文章标识符1687814019897832。
- DOI：`10.1177/1687814019897832`。
- [出版社开放全文](https://journals.sagepub.com/doi/10.1177/1687814019897832)。
- 阅读层级：开放全文，阅读方法、PIV/外特性验证、叶片改型、表3与结论。CC BY 4.0。
- 对象与方法：低比转速离心泵；含旋转曲率修正的IDDES混合模型、边界涡量通量诊断。
- 可用结论：局部PIV显示分离随流量降低而发展，诊断结果用于调整叶片角、包角与出口宽度；高精度价值不仅是性能单值更准，还在于定位需要改型的流动区域。
- 验证范围：有外特性及PIV内流场对照，是说明“性能验证之外还需局部速度场验证”的合适证据。
- 不能推出：性能改进全部来自使用IDDES；表3表示几何改型效果而非模型误差或实验声压。

### 可直接用于Origin的表3数据

以下为论文表3逐项转录；`eta_h`是水力效率，不能标成整机总效率。不是本课程论文新做的实验/仿真，图注须写“据Ren等（2019）表3整理”。保持两位小数，未进行图像数字化。

| Q/Q_BEP | H_before_m | H_after_m | eta_h_before_percent | eta_h_after_percent |
|---:|---:|---:|---:|---:|
| 1.0 | 11.68 | 11.43 | 71.50 | 81.41 |
| 0.8 | 12.50 | 12.89 | 69.06 | 82.40 |
| 0.6 | 13.49 | 13.40 | 65.57 | 76.18 |
| 0.4 | 13.67 | 14.34 | 53.82 | 69.29 |
| 0.2 | 11.96 | 14.00 | 28.03 | 50.20 |

可制作上下双面板：上图绘改型前后H–Q和η_h–Q两组曲线；下图使用相对扬程变化和水力效率百分点变化，显式标注二者定义。该图是“流动诊断支持设计改进”的案例，不能用它作为“LES优于RANS”的定量证明。

## 取舍建议

正文3000字无需把八篇平均分配：P1与P8用于从整体性能转向局部分离；P2/P3解释间距、尾迹与动静干涉如何影响脉动；P4将气核和空化耦合引入“高精度”的定义；P5/P6说明声源和声振传播是另一条验证链。P7与用户熟悉的多级泵激振力可建立联系。若正文另有AI/量子前沿文献，压缩其至展望，不应让算力路线替代泵物理与验证主线。
