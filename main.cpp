#include <algorithm>
#include <cstdint>
#include <iostream>
#include <vector>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n;
    if (!(std::cin >> n)) return 0;
    const int size = n + 2;
    std::vector<std::int64_t> value(size, 1);
    for (int i = 1; i <= n; ++i) std::cin >> value[i];

    // Store each interval in both orientations for contiguous inner-loop reads.
    std::vector<std::int64_t> by_left(size * size, 0);
    std::vector<std::int64_t> by_right(size * size, 0);
    for (int right = 2; right < size; ++right) {
        auto* right_row = by_right.data() + right * size;
        for (int left = right - 2; left >= 0; --left) {
            auto* left_row = by_left.data() + left * size;
            const std::int64_t boundary_product = value[left] * value[right];
            std::int64_t best = 0;
            // The boundary cards survive; last is the final interior card burned.
            for (int last = left + 1; last < right; ++last) {
                best = std::max(best, left_row[last] + right_row[last]
                                     + boundary_product * value[last]);
            }
            left_row[right] = right_row[left] = best;
        }
    }
    std::cout << by_left[size - 1] << '\n';
}
