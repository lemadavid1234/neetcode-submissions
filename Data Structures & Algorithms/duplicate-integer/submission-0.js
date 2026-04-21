class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */


    hasDuplicate(nums) {
        const hasSeen = new Set();

        for (let num of nums) {
            if (hasSeen.has(num)) {
                return true;
            }
            hasSeen.add(num);
        }
        return false;
    }
}
