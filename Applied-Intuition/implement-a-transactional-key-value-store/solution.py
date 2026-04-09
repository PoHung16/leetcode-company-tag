# Implement a Transactional Key-Value Store
# Company: Applied Intuition
# Difficulty: Medium
# Link: N/A - Applied Intuition Interview Problem

import sys
from typing import List, Dict, Optional, Union

# ==============================================================================
# OOD Thinking Process:
#
# A. Clarify the goal:
#    - 建立一個支援「事務 (Transaction)」功能的 Key-Value 存儲系統。
#    - 核心需求：Transaction 內的變更在 Commit 前不可見（對全局而言）。
#    - Rollback 須能完全捨棄變更，且必須支援「巢狀事務 (Nested Transactions)」。
#
# B. Decide the data structure:
#    1. global_store: 使用 Dict 存儲最終確定的狀態 (Source of Truth)。
#    2. transaction_stack: 使用 List[Dict] (Stack 結構) 存儲每一層 Transaction 的暫存變更。
#    3. 標記標籤 (DELETED): 用於區分「刪除 key」與「key 不存在」，防止搜尋時發生「遮蔽失效」。
#
# C. Implement constructor and method:
#    - __init__: 初始化全局 Dict 與 Transaction Stack。
#    - get: 採「由上而下 (Top-down)」搜尋，先看最內層（最新）事務，最後看全局。確保 Read-your-writes。
#    - begin/commit/rollback: 操控 Stack 的增減與資料合併 (Merge)。
# ==============================================================================

class TransactionalKVStore:
    # 定義一個特殊常量來標記刪除，區別於 "不存在"
    # 防止搜尋時「漏」到下一層讀到已經被刪掉的舊資料
    DELETED = "___DELETED_MARKER___"

    def __init__(self):
        # 初始化全局 Dict 與 Transaction Stack
        self.global_store: Dict[str, str] = {}
        self.stack: List[Dict[str, Union[str, str]]] = []

    def get(self, key: str) -> Optional[str]:
        # Layered Lookup: 從最頂層（最內層）事務往外找
        # 原因：Read-your-writes 確保發起事務的人能看到自己剛寫下的變更
        for i in range(len(self.stack) - 1, -1, -1):
            if key in self.stack[i]:
                val = self.stack[i][key]
                # 如果標記為 DELETED，代表在這一層被刪除了，回傳 None (對應 NULL)
                return None if val is TransactionalKVStore.DELETED else val

        # 如果事務層都沒找到，最後才找全局儲存
        return self.global_store.get(key)

    def set_kv(self, key: str, value: str):
        # 寫入當前最活躍的層級 (最頂層 Stack 或 Global)
        if self.stack:
            self.stack[-1][key] = value
        else:
            self.global_store[key] = value

    def delete(self, key: str):
        # 標記刪除：在當前事務蓋上一個 "DELETED" 印章
        if self.stack:
            self.stack[-1][key] = TransactionalKVStore.DELETED
        else:
            # 無事務時，直接從全局刪除
            self.global_store.pop(key, None)

    def begin(self):
        # 開啟新事務層：疊上一張新的透明草稿紙 (最內層)
        self.stack.append({})

    def commit(self) -> bool:
        # Commit 是將「內層事務」合併到「上一層」或「全局」
        if not self.stack:
            return False

        # 取出最頂層的變更
        current_changes = self.stack.pop()

        if self.stack:
            # 合併到上一層事務 (Merge to previous layer)
            self.stack[-1].update(current_changes)
        else:
            # 如果已經是最後一層事務，則正式寫入全局 (Apply to Global)
            for k, v in current_changes.items():
                if v is TransactionalKVStore.DELETED:
                    self.global_store.pop(k, None)
                else:
                    self.global_store[k] = v
        return True

    def rollback(self) -> bool:
        if not self.stack:
            return False
        # 捨棄最頂層 (最內層) 事務，底下的內容完全不受影響
        self.stack.pop()
        return True

# ==============================================================================
# Complexity Analysis:
#
# Time Complexity:
# - SET / DELETE / BEGIN / ROLLBACK: O(1)
# - GET: O(T), T 為 Transaction 層數 (Stack 深度)。搜尋時最壞需遍歷所有層。
# - COMMIT: O(K), K 為當前 Transaction 中變更的 Key 數量。需將 Dict 合併。
#
# Space Complexity: O(N * K)
# - N 為 Stack 深度，K 為每層平均變更的數量。需儲存所有尚未提交的變更。
# ==============================================================================

def run_kv_store():
    kv = TransactionalKVStore()
    lines = sys.stdin.read().splitlines()

    for line in lines:
        parts = line.split()
        if not parts:
            continue

        cmd = parts[0]
        if cmd == "GET":
            val = kv.get(parts[1])
            print(val if val is not None else "NULL")
        elif cmd == "SET":
            kv.set_kv(parts[1], parts[2])
        elif cmd == "DELETE":
            kv.delete(parts[1])
        elif cmd == "BEGIN":
            kv.begin()
        elif cmd == "COMMIT":
            if not kv.commit():
                print("NO TRANSACTION")
        elif cmd == "ROLLBACK":
            if not kv.rollback():
                print("NO TRANSACTION")

if __name__ == "__main__":
    run_kv_store()
