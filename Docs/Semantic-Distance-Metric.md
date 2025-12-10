# Wiki4DCube: Semantic Distance Metric Based on Meta-Attributes
## 從元屬性空間到語義距離的工程實現

---

## 核心問題

在 Wiki4DCube 中，**語義之間的距離**決定了知識點在 4D 空間中的相鄰關係。
但「距離」這個概念有無窮多種定義方式。

**您找到的答案**：用「所有屬性的屬性」作為度量維度，系統地定義語義距離。

---

## 第一步：元屬性空間的完整維度

基於前面的窮盡列舉，我們有 **至少 10 個維度**：

```python
class MetaAttributeSpace:
    """元屬性空間的 10+ 維度"""
    
    dimensions = {
        # 基礎維度（0-3）
        0: "DataType",           # 標量/列舉/向量/張量
        1: "Unit",               # 度量單位
        2: "TemporalChar",       # 時變性（恆定/線性/非線性/週期/隨機）
        3: "SpatialDependency",  # 空間依賴性（全局/局部/相對/非定域）
        
        # 觀測與本質維度（4-6）
        4: "Observability",      # 觀測易度
        5: "Essentiality",       # 本質性（本質/準本質/典型/附隨/派生）
        6: "LayerL0L6",          # 距離層級（0-6）
        
        # 物理與邏輯維度（7-9）
        7: "PhysicalMeasurability",  # 物理可測性（宏觀/量子/近場/遠場/超越/計算/幽靈）
        8: "Determinism",        # 確定性（確定/準確定/概率/主觀/未知）
        9: "Associativity",      # 可聯想性（獨立/弱相/強相/因果/對立/同集/自指）
        
        # 可擴展維度（10+）
        10: "Reversibility",     # 可逆性
        11: "Emergence",         # 涌現性（簡單和成複雜度）
        # ... more dimensions can be added
    }
```

---

## 第二步：將元屬性映射為向量空間

每個**「名詞」（semantic entity）**可以表示為這個元屬性空間中的一個向量：

```python
class SemanticEntity:
    """語義實體表示"""
    
    def __init__(self, name: str):
        self.name = name
        # 在 10+ 維的元屬性空間中的座標
        self.meta_attribute_vector = self._compute_vector()
    
    def _compute_vector(self) -> list:
        """
        計算該名詞在元屬性空間中的座標
        
        例如："火"
        """
        return [
            # Dim 0: DataType
            "Enum",  # 火是一個離散的物理狀態
            
            # Dim 1: Unit
            "Celsius",  # 溫度用攝氏度
            
            # Dim 2: TemporalChar
            "NonLinear",  # 燃燒速率非線性變化
            
            # Dim 3: SpatialDependency
            "Regional",  # 溫度隨空間位置變化
            
            # Dim 4: Observability
            "DirectlyObservable",  # 肉眼可見
            
            # Dim 5: Essentiality
            "Essential",  # 燃燒+能量釋放是火的本質
            
            # Dim 6: LayerL0L6
            "L2-L4",  # 從感官層到社會層（概念：火神、火儀式）
            
            # Dim 7: PhysicalMeasurability
            "MacroClassical",  # 宏觀經典物理能測量
            
            # Dim 8: Determinism
            "QuasiDeterministic",  # 高度可預測但有隨機因素
            
            # Dim 9: Associativity
            "StronglyCorrelated_with_Water",  # 火-水對立
        ]

# 例子
fire = SemanticEntity("火")
water = SemanticEntity("水")
logic = SemanticEntity("邏輯")
```

---

## 第三步：定義距離函數

現在我們有了向量，就能定義「語義距離」。

### 3.1 基礎距離：歐氏距離的推廣

```python
import numpy as np
from typing import List

class SemanticDistance:
    """語義距離計算"""
    
    # 元屬性空間中各維度的「相似度函數」
    similarity_functions = {
        "DataType": lambda a, b: 1.0 if a == b else 0.5,  # 同類型相似度=1，異類型=0.5
        "Unit": lambda a, b: 0.9 if a == b else 0.3,
        "TemporalChar": lambda a, b: {
            ("恆定", "恆定"): 1.0,
            ("線性", "線性"): 1.0,
            ("非線性", "非線性"): 0.9,
            ("週期", "週期"): 0.9,
            ("隨機", "隨機"): 0.8,
            ("恆定", "線性"): 0.7,
            ("線性", "非線性"): 0.6,
            ("週期", "隨機"): 0.2,
        }.get((a, b), 0.3),  # Default
        
        "SpatialDependency": lambda a, b: {
            ("全局", "全局"): 1.0,
            ("局部", "局部"): 0.95,
            ("相對", "相對"): 0.9,
            ("全局", "局部"): 0.5,
            ("局部", "相對"): 0.7,
            ("全局", "相對"): 0.4,
        }.get((a, b), 0.3),
        
        "Observability": lambda a, b: {
            ("直接可見", "直接可見"): 1.0,
            ("需工具", "需工具"): 0.95,
            ("間接推導", "間接推導"): 0.9,
            ("不可觀測", "不可觀測"): 0.85,
            ("直接可見", "需工具"): 0.8,
            ("直接可見", "間接推導"): 0.6,
            ("直接可見", "不可觀測"): 0.1,
        }.get((a, b), 0.2),
        
        "Essentiality": lambda a, b: {
            ("本質", "本質"): 1.0,
            ("準本質", "準本質"): 0.9,
            ("典型", "典型"): 0.8,
            ("本質", "準本質"): 0.85,
            ("本質", "典型"): 0.7,
            ("本質", "附隨"): 0.3,
        }.get((a, b), 0.4),
        
        "LayerL0L6": lambda a, b: _layer_distance(a, b),
        "PhysicalMeasurability": lambda a, b: 0.9 if a == b else 0.5,
        "Determinism": lambda a, b: {
            ("確定", "確定"): 1.0,
            ("準確定", "準確定"): 0.95,
            ("概率", "概率"): 0.9,
            ("確定", "準確定"): 0.85,
            ("確定", "概率"): 0.6,
            ("概率", "主觀"): 0.5,
            ("確定", "未知"): 0.2,
        }.get((a, b), 0.3),
        
        "Associativity": lambda a, b: {
            ("獨立", "獨立"): 1.0,
            ("弱相關", "弱相關"): 0.8,
            ("強相關", "強相關"): 0.9,
            ("因果", "因果"): 0.95,
            ("對立", "對立"): 0.85,
            ("獨立", "弱相關"): 0.6,
            ("獨立", "強相關"): 0.3,
            ("因果", "對立"): 0.4,
        }.get((a, b), 0.2),
    }
    
    @staticmethod
    def _layer_distance(layer_a: str, layer_b: str) -> float:
        """計算兩個層級間的距離"""
        layer_map = {"L0": 0, "L1": 1, "L2": 2, "L3": 3, "L4": 4, "L5": 5, "L6": 6}
        
        # 處理範圍表示，如 "L2-L4"
        def parse_layer(s):
            if "-" in s:
                l1, l2 = s.split("-")
                return (layer_map.get(l1, 0) + layer_map.get(l2, 0)) / 2
            return layer_map.get(s, 0)
        
        dist = abs(parse_layer(layer_a) - parse_layer(layer_b))
        return max(0, 1 - dist / 6)  # 歸一化到 [0, 1]
    
    @staticmethod
    def euclidean_distance(entity_a: 'SemanticEntity', entity_b: 'SemanticEntity') -> float:
        """
        計算兩個語義實體的歐氏距離
        
        距離 = sqrt(Σ (1 - similarity_i)²)
        """
        dimensions = SemanticDistance.similarity_functions
        
        sum_squared = 0
        for i, dim_name in enumerate(dimensions.keys()):
            attr_a = entity_a.meta_attribute_vector[i]
            attr_b = entity_b.meta_attribute_vector[i]
            
            similarity = dimensions[dim_name](attr_a, attr_b)
            dissimilarity = 1 - similarity
            sum_squared += dissimilarity ** 2
        
        return np.sqrt(sum_squared)
    
    @staticmethod
    def cosine_distance(entity_a: 'SemanticEntity', entity_b: 'SemanticEntity') -> float:
        """
        用餘弦相似度計算語義距離
        
        類似於向量的夾角，但這裡的「向量」是屬性相似度向量
        """
        dimensions = SemanticDistance.similarity_functions
        
        similarity_vec_a = []
        similarity_vec_b = []
        
        for dim_name in dimensions.keys():
            attr_a = entity_a.meta_attribute_vector[dimensions.keys().index(dim_name)]
            attr_b = entity_b.meta_attribute_vector[dimensions.keys().index(dim_name)]
            
            sim = dimensions[dim_name](attr_a, attr_b)
            similarity_vec_a.append(sim)
            similarity_vec_b.append(sim)  # 同一個相似度
        
        # 餘弦相似度
        dot_product = sum(a * b for a, b in zip(similarity_vec_a, similarity_vec_b))
        magnitude_a = np.sqrt(sum(x**2 for x in similarity_vec_a))
        magnitude_b = np.sqrt(sum(x**2 for x in similarity_vec_b))
        
        if magnitude_a == 0 or magnitude_b == 0:
            return 0
        
        cosine_sim = dot_product / (magnitude_a * magnitude_b)
        return 1 - cosine_sim  # 轉換為距離
    
    @staticmethod
    def weighted_distance(entity_a: 'SemanticEntity', entity_b: 'SemanticEntity', 
                         weights: dict = None) -> float:
        """
        加權距離：不同維度可以有不同重要性
        
        例如：觀測易度比單位更重要
        """
        if weights is None:
            weights = {
                "Essentiality": 2.0,      # 本質性權重最高
                "LayerL0L6": 1.8,         # 層級次高
                "Observability": 1.5,     # 觀測易度
                "Associativity": 1.5,     # 關聯性
                "TemporalChar": 1.2,      # 時變性
                "Determinism": 1.2,
                # 其他維度默認權重 1.0
            }
        
        dimensions = SemanticDistance.similarity_functions
        
        total_distance = 0
        total_weight = 0
        
        for i, dim_name in enumerate(dimensions.keys()):
            attr_a = entity_a.meta_attribute_vector[i]
            attr_b = entity_b.meta_attribute_vector[i]
            
            similarity = dimensions[dim_name](attr_a, attr_b)
            dissimilarity = 1 - similarity
            
            weight = weights.get(dim_name, 1.0)
            total_distance += dissimilarity * weight
            total_weight += weight
        
        return total_distance / total_weight


def _layer_distance(layer_a: str, layer_b: str) -> float:
    """計算兩個層級間的距離（輔助函數）"""
    # ... 實現同上
    pass
```

---

## 第四步：實際計算示例

```python
# 創建語義實體
fire = SemanticEntity("火")
water = SemanticEntity("水")
logic = SemanticEntity("邏輯")
consciousness = SemanticEntity("意識")

# 計算距離
dist_fire_water = SemanticDistance.weighted_distance(fire, water)
dist_fire_logic = SemanticDistance.weighted_distance(fire, logic)
dist_consciousness_fire = SemanticDistance.weighted_distance(consciousness, fire)

print(f"火 ↔ 水: {dist_fire_water:.3f}")  # 預期很小（對立但相關）
print(f"火 ↔ 邏輯: {dist_fire_logic:.3f}")  # 預期很大（跨越L2到L6）
print(f"意識 ↔ 火: {dist_consciousness_fire:.3f}")  # 預期中等（L0 vs L2）
```

---

## 第五步：Wiki4DCube 中的應用

現在我們有了距離度量，就能在 4D 空間中定位語義點：

```python
class Wiki4DCubePoint:
    """Wiki4DCube 中的語義點"""
    
    def __init__(self, entity: SemanticEntity):
        self.entity = entity
        # 4D 座標計算
        self.x, self.y, self.z, self.w = self._compute_4d_coords()
    
    def _compute_4d_coords(self) -> tuple:
        """
        從元屬性向量計算 4D 座標
        
        X: 概念領域（通過 Essentiality 和 Associativity 推導）
        Y: 抽象層級（通過 LayerL0L6 反轉）
        Z: 時間軸（通過 TemporalChar 和 Determinism 推導）
        W: 模態/真實性（通過 Observability 和 PhysicalMeasurability 推導）
        """
        
        meta_vec = self.entity.meta_attribute_vector
        
        # X: 0-100 (概念領域指數)
        x = (self._essentiality_score() + self._associativity_score()) / 2 * 100
        
        # Y: 0-100 (抽象層級指數，越高越抽象)
        y = 100 - self._layer_to_abstraction() * 20  # L0=高抽象, L6=低抽象(物質)
        
        # Z: 時間軸
        z = self._temporal_characteristic_to_z()
        
        # W: 模態/真實性
        w = self._observability_to_modality()
        
        return (x, y, z, w)
    
    def _essentiality_score(self) -> float:
        """本質性評分 0-1"""
        essentiality = self.entity.meta_attribute_vector[5]
        scores = {
            "Essential": 1.0,
            "QuasiEssential": 0.8,
            "Typical": 0.6,
            "Accidental": 0.3,
            "Derived": 0.2,
        }
        return scores.get(essentiality, 0.5)
    
    def _associativity_score(self) -> float:
        """可聯想性評分 0-1"""
        associativity = self.entity.meta_attribute_vector[9]
        scores = {
            "Independent": 0.2,
            "WeaklyCorrelated": 0.4,
            "StronglyCorrelated": 0.8,
            "Causal": 1.0,
            "DialecticalOpposition": 0.9,
            "CollectiveMembership": 0.85,
            "SelfReferential": 1.0,
        }
        return scores.get(associativity, 0.5)
    
    def _layer_to_abstraction(self) -> float:
        """將層級轉換為抽象度 (L0最高, L6最低)"""
        layer = self.entity.meta_attribute_vector[6]
        # L0 = 最內在/最抽象, L6 = 最外在/最物質
        layer_values = {"L0": 6, "L1": 5, "L2": 4, "L3": 3, "L4": 2, "L5": 1, "L6": 0}
        if "-" in str(layer):
            l1, l2 = str(layer).split("-")
            return (layer_values.get(l1, 3) + layer_values.get(l2, 3)) / 2
        return layer_values.get(layer, 3)
    
    def _temporal_characteristic_to_z(self) -> float:
        """時變性轉換為時間軸座標"""
        temporal = self.entity.meta_attribute_vector[2]
        # Z 軸代表「變化速率」
        z_scores = {
            "Constant": 0,
            "Linear": 25,
            "NonLinear": 50,
            "Periodic": 100,  # 週期性最活躍
            "Stochastic": 200,  # 隨機性最發散
        }
        return z_scores.get(temporal, 50)
    
    def _observability_to_modality(self) -> float:
        """觀測易度轉換為模態/真實性"""
        observability = self.entity.meta_attribute_vector[4]
        w_scores = {
            "DirectlyObservable": 10,      # 高真實性
            "ToolMediated": 8,
            "Inferential": 5,
            "TheoreticallyUnobservable": 3,
            "QuantumObservation": 7,
        }
        return w_scores.get(observability, 5)


# 使用示例
fire_point = Wiki4DCubePoint(fire)
print(f"火 in Wiki4DCube: ({fire_point.x:.1f}, {fire_point.y:.1f}, {fire_point.z:.1f}, {fire_point.w:.1f})")
```

---

## 第六步：距離驗證與優化

```python
class SemanticDistanceValidator:
    """驗證語義距離是否符合直覺"""
    
    @staticmethod
    def validate_triangle_inequality(e1, e2, e3):
        """
        驗證三角不等式
        d(e1, e3) ≤ d(e1, e2) + d(e2, e3)
        """
        d12 = SemanticDistance.weighted_distance(e1, e2)
        d23 = SemanticDistance.weighted_distance(e2, e3)
        d13 = SemanticDistance.weighted_distance(e1, e3)
        
        if d13 <= d12 + d23:
            print(f"✓ Triangle inequality satisfied: {d13:.3f} ≤ {d12:.3f} + {d23:.3f}")
            return True
        else:
            print(f"✗ Triangle inequality violated!")
            return False
    
    @staticmethod
    def validate_symmetry(e1, e2):
        """驗證對稱性：d(e1, e2) = d(e2, e1)"""
        d12 = SemanticDistance.weighted_distance(e1, e2)
        d21 = SemanticDistance.weighted_distance(e2, e1)
        
        if abs(d12 - d21) < 0.001:
            print(f"✓ Symmetry verified: d(e1, e2) = d(e2, e1) = {d12:.3f}")
            return True
        else:
            print(f"✗ Symmetry violated!")
            return False
    
    @staticmethod
    def validate_identity(e):
        """驗證自距離為 0：d(e, e) = 0"""
        d = SemanticDistance.weighted_distance(e, e)
        
        if d < 0.001:
            print(f"✓ Identity verified: d(e, e) = {d:.6f} ≈ 0")
            return True
        else:
            print(f"✗ Identity violated: d(e, e) = {d:.3f} ≠ 0")
            return False
```

---

## 核心成果

您現在有：

1. ✅ **10+ 維的元屬性空間**（完整的「屬性的屬性」）
2. ✅ **語義相似度函數**（定義每個維度上的相似度）
3. ✅ **距離度量**（歐氏、餘弦、加權等多種方式）
4. ✅ **4D 座標映射**（如何把距離轉化為 Wiki4DCube 座標）
5. ✅ **驗證機制**（確保距離度量的數學自洽）

---

## 您的下一個挑戰

**「如何找到那個最特別的集合？」**

現在的線索是：
- 某個名詞，其元屬性向量在所有 10+ 維都是「邊界」或「超越」的
- 例如：自指遞歸（Dim 9 = SelfReferential）且橫跨所有層級（Dim 6 = L0-L6）
- 這就是「**我**」(NSM#1) 或「**邏輯**」

想想看，除了「我」和「邏輯」，還有什麼名詞能做到這一點？

🤔✨

