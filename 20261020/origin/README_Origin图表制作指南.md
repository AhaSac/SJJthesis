# 泵 CFD 精度综述：四套 Origin 多面板图

这份指南是作图设计和可导入数据包。图1、图4已有原文公开表格数据，可以现在制作；图2、图3只有表头，需补充自己的 Fluent 时序和收敛算例后才能画结果。空白不是零值，不能连成曲线。未生成或假造任何实验数据、噪声曲线、模型评分。

课程论文约三千字，建议正文选图1和图4，图2、图3用作后续研究方案。最终正文图号由实际插入顺序决定，这里的01—04是文件编号。

## 共同版式与导入

1. 在 Origin 新建工作簿，直接拖入 CSV，或使用 ASCII/CSV 导入；第一行设为列长名称，不作为数据。文件是 UTF-8。将 `NA`、空白设为缺失值，不替换为0。
2. 在列属性设置 X/Y 角色、Long Name 和 Units。以下表头包含单位，但坐标轴仍需明确写单位。分类列设为 Text & Numeric/Categorical；网格数量和流量列保持数值型。
3. 单图宽约160 mm，三面板横排的高度约65—80 mm；2×2面板用160×125 mm。图内中文宋体9—10 pt、英文和数字 Times New Roman 9—10 pt，面板标记(a)(b)(c)用10 pt。字号仅是绘图建议，不替代论文标题/正文格式。
4. 蓝色 `#0077BB` 配实线圆点，橙色 `#EE7733` 配虚线方点，灰色作辅助线。保留符号差异，兼顾黑白打印。网格线只用浅灰主网格，不用渐变背景或柱体立体效果。
5. 分别画子图后，使用 Graph → Merge Graph Windows 合并，设置统一面板宽度；只对含义相同的轴联动。保留(a)—(c)标记，删除重复的图内总标题，完整说明写在论文图注。
6. 导出 PDF 矢量图并嵌入字体，同时可留600 dpi PNG预览。建议文件名 `fig01_grid.pdf`、`fig02_convergence.pdf`、`fig03_spectra.pdf`、`fig04_redesign.pdf`。无需安装新的第三方作图软件。Origin版本/语言不同，菜单名称可能略有区别。

## 图1：平均性能量的网格敏感性（三面板，真实数据）

### 数据及出处

- `01_grid_original_Li2021.csv`：逐项转录原文Table 3中的网格数、扬程系数、功率系数。
- `01_grid_recalculated_Li2021.csv`：使用上述四组原始值计算归一化网格尺度、相对最细网格的差异。
- Li, Kunhang; Xu, Wenqian; Dou, Hua-Shu. *Flow Stability in a Miniature Centrifugal Pump under the Periodic Pulse Flow*. **Energies**, 2021, 14(24), 8338. [原文及Table 3](https://www.mdpi.com/1996-1073/14/24/8338)，[DOI](https://doi.org/10.3390/en14248338)，[出版社公开PDF](https://mdpi-res.com/d_attachment/energies/energies-14-08338/article_deploy/energies-14-08338-v2.pdf)。核验日期：2026-10-20。原文采用CC BY 4.0。

这是微型离心泵的SST k-ω算例。系数按原文定义原样使用，不与其他文献采用不同转速/半径约定的系数直接拼接。该表只支撑平均性能量的网格敏感性讨论。

### 数据字典和计算

| 列 | 含义、单位、公式 |
|---|---|
| `N_million` | 网格单元总数，以百万计，实际数为本列×10⁶ |
| `HeadCoefficient` | 原文扬程系数，无量纲 |
| `PowerCoefficient` | 原文功率系数，无量纲 |
| `h_over_hfinest` | `(10.80/N_million)^(1/3)`；仅在域体积相同下作为有效尺度代理 |
| `Head_over_finest` | `HeadCoefficient/0.001661`，无量纲 |
| `Power_over_finest` | `PowerCoefficient/0.00001839`，无量纲 |
| `HeadDifference_finest_pct` | `100*(HeadCoefficient/0.001661-1)`，% |
| `PowerDifference_finest_pct` | `100*(PowerCoefficient/0.00001839-1)`，% |

这里使用带符号差异，四组数据恰好均非负。相对最细网格差异不等于相对真实解的误差。原文的Relative Change是逐级网格变化，不能直接作为本图(b)数据。本表的6.68百万网格相对最细网格差异约为扬程系数0.301%、功率系数0.163%。不能由此宣称瞬态激振力/宽带噪声已收敛。

### 面板及 Origin 操作

1. (a) X=`N_million`，左Y=`HeadCoefficient`，右Y=`PowerCoefficient`。用双Y轴线+符号图，左轴用×10⁻³、右轴用×10⁻⁵显示科学计数。两种系数独立轴，分别配同色轴标题；轴上下限从数据范围取，不人为调成两曲线重合。双轴只展示各自变化，斜率不能横向比较。
2. (b) X=`N_million`，Y为两列`Difference_finest_pct`，画同轴线+符号图。Y轴标题“相对最细网格差异 / %”，加Y=0参考线。4点保留可见，不做多项式拟合。
3. (c) 将整表复制到新表，按`h_over_hfinest`从小到大整行排序。以其为X，两个`over_finest`列为Y画线+符号图，加Y=1虚线。标明“有效网格尺度代理”，与(a)(b)一并合并成1×3图。
4. 在(a)用竖向浅灰辅助线标记原文采用的6.68百万网格；辅助线文字只写“原文后续计算网格”。

**图注可用：** 微型离心泵平均性能量的网格敏感性。(a)扬程系数和功率系数；(b)相对10.80百万单元网格的差异；(c)按有效网格尺度归一化的性能量。数据据Li等（2021）Table 3重绘，归一化和差异由本文计算。最细网格仅作为比较基准，未进行Richardson外推或GCI估计。

**边界：** 总网格数并不能代表叶缘、间隙和壁面各方向的局部加密，故不拟合形式收敛阶、不绘制GCI条带；更不能把本图称为LES精度比较。

## 图2：空间、时间与采样长度的三级收敛图（3×3面板，待真实数据）

### 设计与试验控制

九个面板按行分别是空间网格、求解时间步、保留采样时长；按列分别是平均扬程、Fx的BPF窄带RMS、压力宽带RMS。这样能直观看出平均量接近稳定时，非定常指标是否还在变化。

每次只改变一个控制量：空间组固定求解时间步与分析设置；时间组固定网格、保留时长与公共可解析频带；时长组从同一稳定后的长序列取逐步延长的片段，固定Welch段长、窗、重叠和频带。时长组各点相互嵌套，不能当成独立重复样本。模型、转速、流量、测点必须相同。

### 表头及字段

`02_convergence_template.csv`一行代表一个算例和一套分析设置。

| 字段 | 说明 |
|---|---|
| `series_id,case_id` | 同一单因素系列标识、唯一算例标识，文本 |
| `study_axis` | 仅填`space`、`time`或`duration` |
| `model` | 求解模型原名，如SST-URANS、IDDES，不能填主观精度等级 |
| `N_cells,dt_s,sample_dt_s` | 单元总数；求解时间步(s)；实际导出采样间隔(s)，后二者可能不同 |
| `n_rpm,Z,retained_T_s` | 转速(r/min)、叶片数、去掉初始过渡后保留的时长(s) |
| `Welch_segment_L,Welch_overlap_samples` | 每段样本数、重叠样本数，整数 |
| `f_low_Hz,f_high_Hz,BPF_halfband_Hz` | 预先约定的宽带积分范围与BPF积分半宽，Hz；宽带需排除哪些离散线及其泄漏范围写入notes |
| `H_mean_m` | 稳定区间平均扬程，m |
| `Fx_BPF_band_rms_N` | `sqrt(∫S_FxFx(f)df)`，积分区间为BPF±指定半宽，N |
| `p_broadband_rms_Pa` | 宽带积分`∫S_pp(f)df`后开方，Pa；按notes剔除预定离散线频带 |
| `reference_case_id` | 本系列最细网格/最小时间步/最长时长算例ID |
| 三列`*_rel_difference_pct` | `100*abs(q-q_ref)/abs(q_ref)`；参考值为0时填NA，改报有单位的绝对差 |
| `source_file,notes` | 原始导出文件名与处理说明；明确压力测点、力的积分表面/分量、宽带定义 |

转频`f_r=n_rpm/60`，BPF=`Z*f_r`；每转角步长`Δθ=6*n_rpm*dt_s`（°），保留转数`R=n_rpm*retained_T_s/60`。采样Nyquist频率为`1/(2*sample_dt_s)`，不能用求解步长替代实际导出间隔。

若同高程、液体近似不可压，扬程可按两截面质量流量加权平均总压差`H=(p_t,out-p_t,in)/(ρg)`计算；有高差且总压不含重力势时补`z_out-z_in`。转矩均值不自动等于水力效率。所有系列须固定同一物理量定义。

### Origin 操作

1. 用筛选器分别筛出三组数据，不把不同模型混入同一收敛系列。空间组新增X=`(N_ref/N_cells)^(1/3)`，时间组新增X=`6*n_rpm*dt_s`，时长组新增X=`n_rpm*retained_T_s/60`。
2. 每组按X排序，三列响应分别作线+符号图。建议主图画有单位的原值；每格右上角小窗画该指标相对本系列参考值的差异。轴标题分别是m、N、Pa，不能叠到同一Y轴。
3. 添加参考值水平虚线；若有预先确定的工程容许差，可另加阈值线并注明“本研究验收阈值”。不能擅填通用的1%或5%合格线。
4. 合并3×3图，列标题写“平均扬程 / BPF力 / 宽带压力”，行标题写“空间 / 时间 / 采样”。仅在相同物理量列共享Y轴范围。
5. 只有在真正独立重复样本或合理分块估计后，才能添加统计误差棒，并注明置信度和估计方法。残差下降不能作为误差棒。

**待补：** 至少三套空间网格、三档时间步、一份足够长且已稳定的等间隔多通道时序；各组完整物理和数值设置。目前CSV只有表头，不能作为已完成结果使用。

**完成后的图注模板：** 泵平均性能及非定常载荷的空间、时间和采样时长敏感性。各系列采用[模型、工况]，只改变对应控制量；BPF窄带为[频带]，宽带为[频带及排除频带]。小窗为相对各系列参考算例的差异，参考算例不代表精确解。

## 图3：周向压力谱、激振力相干与相位（四面板，待真实时序）

### 四面板布局

(a)周向测点角度θ—轴阶次`o=f/f_r`—压力PSD的3D瀑布线；(b)同一数据的θ×阶次二维热图；(c)一个明确测点压力与Fx的幅值平方相干曲线；(d)相应互谱相位曲线。两个频谱视图互补：瀑布看频率峰形，热图看周向分布。不要把非等角测点人为放成等距角度。

测点优先在同一静止截面同半径周向布置，记录角度零点与正向。所有压力、力通道需同一采样时钟。若用了转动坐标系测点，单独标注并说明如何转换，不能与静止测点角度直接混用。

### 文件与字段

- `03_timeseries_template.csv`：time单位s，p01—p06单位Pa，可增减测点列；Fx/Fy/Fz单位N，是指定表面上同一坐标系的流体力。压力输入可以是表压，但必须明确压力类型并去均值；不要用绝对静压当声压。
- `03_monitor_metadata_template.csv`：`monitor_id`与p01等一致；`theta_deg`为物理角度(°)，xyz为坐标(m)；`stationary_or_rotating_frame`标坐标系；`location_description`写叶缘/蜗舌/出水管等位置；`pressure_type`写静压/总压及表压/绝对压；`source_file`记录出处。
- `03_psd_long_template.csv`：每行一个测点一个频率。`PSD_p_Pa2_per_Hz`单位Pa²/Hz，其余运行/处理参数见图2；`shaft_order=f_Hz/(n_rpm/60)`无量纲；`window`填实际周期Hann等，`detrend=segment_mean`，`scaling=onesided_density`。
- `03_coherence_phase_template.csv`：Spp单位Pa²/Hz，SFF单位N²/Hz，SpF实部/虚部单位Pa·N/Hz；相干无量纲，phase单位°。`pressure_monitor_id,force_component`标明参与的两通道，不能只写“力压相干”。

### 必须固定的谱估计定义

均匀采样`f_s=1/Δt_s`。每段L个点、相邻段50%重叠可作为起点，段内去均值，周期Hann窗`w[j]=0.5-0.5*cos(2πj/L)`。设`U=Σw[j]²`，DFT按未除L的定义计算。对每个分段k得到`P_k(f)`，单边Welch压力PSD为

`S_pp(f_l) = a_l/(K*f_s*U) * Σ_k |P_k(f_l)|²`。

`a_l`在DC及偶数L时Nyquist点为1，其余正频率为2；K为分段数。段频率格点间距`Δf=f_s/L`；Hann窗实际分辨能力还受主瓣宽度影响。零填充只加密频率显示格点，不提高实际频率分辨率。整段长度给出可观测低频范围，段长度决定Welch频率分辨能力，二者要一起报告。

互谱采用`S_pF=a_l/(K*f_s*U)*Σ_k conj(P_k)*F_k`，且

`γ²_pF=|S_pF|²/(S_pp*S_FF)`，`φ_pF=atan2(Im(S_pF),Re(S_pF))*180/π`。

在此约定下，F相对p延迟τ会给负相位`φ≈-2πfτ`。交换输入通道会反转相位符号；先平均互谱，再求相位，不平均分段相位角。低相干区域相位不稳定，不作传播时延解释；只保留一段数据会使相干估计退化，必须有充分分段。高相干表明线性频域关联，不证明因果或声辐射来源。

上述归一化与[Welch官方实现说明](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.welch.html)、[互谱约定](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.csd.html)、[相干定义](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.coherence.html)一致；这些链接用于核对数学定义，并不要求安装Python库。

`∫S_pp df`近似等于按同样分段/去趋势/窗处理的均方值。PSD峰高不是单频RMS幅值：离散峰需在预先确定的频带内积分，再开方。若只是把横坐标Hz换成阶次，纵轴仍可保留Pa²/Hz；如果改成“每阶次密度”，必须同时变换`S_order(o)=f_r*S_f(f_r*o)`，不能只改单位标签。

### Origin 操作

1. 导入等间隔原始时序，核对时间差恒定及稳定区间。用列统计先核对均值/RMS；保存未处理时序和截取范围。
2. 若已安装OriginLab官方Power Spectral Density应用，选Method=Welch，设Hann/Hanning窗、L、50%重叠、单边density。详见[OriginLab应用说明](https://cloud.originlab.com/fileExchange/details.aspx?fid=1006)。无需为本任务安装该应用；若没有，使用下一步的工作表分段方法。
3. 工作表分段方法：将时序按L分成多段并按L/2滑动，每段减其均值并乘上述窗；用Origin FFT工具获取**未归一化复数DFT**。若工具自动除L，先恢复乘L；逐频计算模方/互谱，按前述公式跨段平均。由DFT复数值按公式计算最稳妥，不能把界面“Amplitude/Power”列直接当Pa²/Hz。保存L、U、K、f_s；用均方积分校验归一化后再填入CSV。
4. Origin内置窗函数列表的“Welch”是一种窗，**不是Welch分段平均方法**。本指南选的是Hann窗与Welch方法的组合，不能混淆。
5. 对长表按monitor_id透视/拆列，得到A列阶次、后续列各θ下PSD，做3D Waterfall；Y方向使用真实θ坐标。若版本的瀑布仅按序号排布，轴写“测点序号”，刻度明确对应θ。另将长表设为XYZ并透视为θ×阶次矩阵，做Color Fill/Heatmap。优先保留原网格，不用高阶插值生成额外峰。
6. PSD可用对数颜色/高度轴，标Pa²/Hz；零值和缺测遮罩，不人为加小正数。叠加转频、BPF及其谐波参考线：轴阶次分别是1、Z、2Z。若只用BPF归一化横轴，必须另写`f/f_BPF`，此时BPF位于1。
7. 有OriginPro可用Analysis → Signal Processing → Coherence，参数与PSD一致，按[官方说明](https://docs.originlab.com/origin-help/cohere/)核对。若没有Pro，只用前述分段复数互谱工作表计算相干。相位从SpF实/虚部计算；数学atan2的两个参数顺序以软件帮助为准。
8. 相干Y范围0—1，相位Y范围−180°—180°，低相干处灰化并注明筛选规则。将四幅图合成2×2图。不得拿瞬时Fx与非同步压力采样做相干。

**声学量边界：** 叶面/壁面压力含流体动力压力，PSD本身不是远场声压级。真正声学测点才用`L_p=20*log10(p_rms/p_ref)`；水声常用`p_ref=1 μPa`，空气常用`20 μPa`，必须标明介质、频带、距离与参考值。频带声压级亦可写`10*log10(∫S_pp df / p_ref²)`。不能直接把Pa²/Hz代入20log公式，也不能把单点PSD的10log值称为总声压级。本图默认不转换声压级。

**待补：** 至少数个周向测点和同步力序列，确切测点坐标、导出间隔、转速、叶片数、保留时长；PSD和互谱需由相同分析参数得到。无原始时序时不做演示正弦信号替代。

**完成后的图注模板：** [工况]泵内周向压力谱及其与[表面]Fx的频域关联。(a)单边压力PSD瀑布图；(b)同数据的周向谱图；(c)[测点]压力—Fx幅值平方相干；(d)按conj(P)F约定计算的互谱相位。采样间隔为[ ]s，稳定序列长[ ]s，Welch采用周期Hann窗、L=[ ]点、重叠[ ]点。BPF阶次为Z=[ ]；该压力为泵内流体动力压力，未直接等同于远场噪声。

## 图4：高保真流场诊断支持叶轮改型（四面板，真实数据）

### 数据与证据性质

Ren, Yun; Zhu, Zuchao; Wu, Denghao; Li, Xiaojun; Jiang, Lanfang. *Investigation of flow separation in a centrifugal pump impeller based on improved delayed detached eddy simulation method*. **Advances in Mechanical Engineering**, 2019, 11(12), 1–13. [出版社原文、Table 3](https://journals.sagepub.com/doi/10.1177/1687814019897832)，[DOI](https://doi.org/10.1177/1687814019897832)。核验日期：2026-10-20。

`04_redesign_original_Ren2019.csv`逐项转录Table 3。原文先对方法作外特性与PIV验证，再将改型叶轮重新建模、划网格并用相同方法计算。因此这里标为“原文改型分析中的数值性能指标”，不能标成改型样机实验。方法为含旋转/曲率修正的IDDES框架；该图比较几何改型，不能用来论证IDDES比URANS准确多少。

### 数据字典

| 列 | 单位与定义 |
|---|---|
| `Q_over_QBEP` | 流量与原文基准BEP流量之比，无量纲；两个方案共用该基准 |
| `H_before_m,H_after_m` | 原型/改型扬程，m |
| `eta_h_before_pct,eta_h_after_pct` | 水力效率，%；不能称整泵总效率 |
| `Delta_H_m` | `H_after_m-H_before_m`，m |
| `Delta_H_relative_pct` | `100*(H_after_m/H_before_m-1)`，% |
| `Delta_eta_h_percentage_points` | `eta_h_after_pct-eta_h_before_pct`，百分点(pp) |
| `Delta_eta_h_relative_pct` | `100*(eta_h_after_pct/eta_h_before_pct-1)`，% |

### Origin 操作

1. 导入`04_redesign_recalculated_Ren2019.csv`，**整行**按`Q_over_QBEP`从0.2到1.0升序排序。禁止只排X列使数据错位。
2. (a)两列H画线+符号图；(b)两列ηh画线+符号图。原型统一蓝色空心圆、改型统一橙色实心方块。两面板共用流量X轴。
3. (c)`Delta_H_relative_pct`画柱图，Y=0加黑色参考线，负增量保留；(d)`Delta_eta_h_percentage_points`画柱图，纵轴写“水力效率增量 / pp”。这比同轴把百分比和百分点混画更清楚。
4. 将(a)(b)(c)(d)合成2×2图，顶排性能、底排增量。只画五个真实工况点之间的直线辅助连线，不做样条外推、不拟合新峰值、不画没有数据的误差棒。
5. 如希望再加数值标签，(d)仅显示1位或2位小数；原表精度为0.01，不能让CSV计算产生的小数位数暗示更高测量精度。

**图注可用：** 流场诊断支持的离心泵叶轮改型效果。(a)扬程；(b)水力效率；(c)扬程相对变化；(d)水力效率的百分点增量。原型与改型数据据Ren等（2019）Table 3重绘，增量由本文计算。所示为原文改型分析的数值性能指标，不代表不同湍流模型的精度比较；原表未提供改型噪声或相应统计不确定度。

## 与正文衔接及使用顺序

图1说明“平均指标需要网格检查，但检查的指标范围有限”；图4说明“更细的流动机理诊断如何服务设计修改”。图2、图3承接用户当前Fluent工作流：平均扬程/转矩之后，进一步检查时间分辨、统计采样、谱能量和载荷关联。

后续若加入效率—压力脉动—噪声Pareto图，须在同工况、同介质、同声学观察位置下取得全部指标，并先说明约束与支配关系；现有两篇表格没有噪声和不确定度数据，不能补成“综合优势评分”或声学Pareto前沿。

## LaTeX 插入方式（不自动插入未完成图）

当前采用单文件项目：将Origin导出的PDF直接放入`20261020/sjj22627171/`。`fig01_grid.pdf`和`fig04_redesign.pdf`会由唯一tex中的图件接口自动插入。其他新增图片可在同一tex正文适当位置使用以下代码：

```latex
\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.97\linewidth]{fig01_grid.pdf}
  \caption{微型离心泵平均性能量的网格敏感性。数据据原文Table 3重绘。}
  \label{fig:grid-sensitivity}
\end{figure}
```

按项目最终bib键在完整图注中补`\cite{...}`，不要把占位键留在提交稿中。
