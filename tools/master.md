# JS, C++, Python

```
Description: Similar
```

# Lambda: map
```
# JS
numbers = [1,2,3,4];                                                    numbers = Array(1, 2, 3, 4);                       
const doubled = numbers.map(x => x * 2);
console.log(doubled);

# Python
numbers: list[int] = [1,2,3,4]
doubled: list[int] = [i * 2 for i in numbers]
print(doubled)

# C++
#include <iostream>     // std::cout
#include <algorithm>    // std::transform
#include <iterator>     // std::begin, std::end                         // #include <vector>

int main() {
    int numbers[] = {1, 2, 3, 4};                                       std::vector<int> numbers = {1, 2, 3, 4};
    int doubled[4];                                                     std::vector<int> doubled(4);
    // C++11 (transform)
    std::transform(std::begin(numbers), std::end(numbers),              std::transform(numbers.begin(), numbers.end(),
        doubled,                                                            doubled.begin(),             
        [](int x) { return x * 2; });                                       [](int x) { return x * 2; });

    // C++20 (ranges) has pipeline
    // auto doubled = numbers | std::views::transform([](int x){ return x * 2; });

    for (int x : doubled) {                                             for (int x : doubled) {
        std::cout << x << " ";                                              std::cout << x << " ";
    }                                                                   }
    return 0;
}
```

# Lambda: filter
```
# JS
numbers = [1,2,3,4];                                                    numbers = Array(1, 2, 3, 4);
const evens = numbers.filter(x => x % 2 === 0);
console.log(evens)

# Python
numbers: list[int] = [1,2,3,4]
evens = [x for x in numbers if x % 2 == 0]
print(evens)

# C++
#include <iostream>             // std::cout
#include <vector>               // std::vector
#include <algorithm>            // std::copy_if
#include <iterator>             // std::back_inserter

int main() {
    std::vector<int> numbers = {1, 2, 3, 4};
    std::vector<int> evens;

    // C++11
    std::copy_if(numbers.begin(), numbers.end(),
        std::back_inserter(evens),
        [](int x){ return x % 2 == 0; });

    // C++20
    // auto evens = numbers | std::views::filter([](int x){ return x % 2 == 0; });

    for (int x : evens) {
        std::cout << x << " ";
    }

    return 0;
}
```

# Lambda: reduce
```
# JS
numbers = [1,2,3,4];                                                    numbers = Array(1, 2, 3, 4);
const sum = numbers.reduce((a, b) => a + b);

# Python
from functools import reduce

numbers = [1,2,3,4]
sum_val = reduce(lambda a, b: a + b, numbers)
# Pythonic:
sum_val = sum(numbers)
print(sum_val)

# C++ (std::accumulate)
#include <iostream>         // std::cout
#include <vector>           // std::vector
#include <numeric>          // std::accumulate

int main() {
    std::vector<int> numbers = {1, 2, 3, 4};

    // C++ (std::accumulate)
    // accumulate(begin, end, initial_value)
    int sum = std::accumulate(numbers.begin(), numbers.end(), 0);

    // C++20
    // #include <ranges>
    // int sum = std::ranges::fold_left(numbers, 0, std::plus<>());

    std::cout << "Sum = " << sum << std::endl;

    return 0;
}
```

# Lambda: find
```
# JS
numbers = [1,2,3,4];                                                    numbers = Array(1, 2, 3, 4);
const found = numbers.find(x => x === 3);

# Python
numbers = [1,2,3,4]
found = next((x for x in numbers if x == 3), None)
print(found)

# C++
#include <iostream>      // std::cout
#include <vector>        // std::vector
#include <algorithm>     // std::find

int main() {
    std::vector<int> numbers = {1, 2, 3, 4};

    // C++ (std::find)
    // std::find(begin, end, value) returns an iterator to the first occurrence
    auto it = std::find(numbers.begin(), numbers.end(), 3);

    // Check if found
    if (it != numbers.end()) {
        int found = *it;  // dereference iterator to get value
        std::cout << "Found: " << found << std::endl;
    } else {
        std::cout << "Value not found" << std::endl;
    }

    return 0;
}
```

# Lambda: some/any
```
# JS
numbers = [1,2,3,4];                                                    numbers = Array(1, 2, 3, 4);
const hasEven = numbers.some(x => x % 2 === 0);

# Python
numbers = [1,2,3,4]
has_even = any(x % 2 == 0 for x in numbers)
print(has_even)

# C++
#include <iostream>      // std::cout
#include <vector>        // std::vector
#include <algorithm>     // std::any_of

int main() {
    std::vector<int> numbers = {1, 2, 3, 4};

    // C++ (std::any_of)
    // std::any_of(begin, end, predicate) returns true if any element satisfies the predicate
    bool hasEven = std::any_of(numbers.begin(), numbers.end(),
        [](int x){ return x % 2 == 0; });

    if (hasEven) {
        std::cout << "The list has at least one even number." << std::endl;
    } else {
        std::cout << "No even numbers found." << std::endl;
    }

    return 0;
}
```

# Lambda: every/all
```
# JS
numbers = [1,2,3,4];                                                    numbers = Array(1, 2, 3, 4);
const allPositive = numbers.every(x => x > 0);

# Python
numbers = [1,2,3,4]
all_positive = all(x > 0 for x in numbers)
print(all_positive)

# C++
// C++
#include <iostream>      // std::cout, std::endl
#include <vector>        // std::vector
#include <algorithm>     // std::all_of

int main() {
    std::vector<int> numbers = {1, 2, 3, 4, 5};

    // C++ (std::all_of)
    // std::all_of(begin, end, predicate) returns true if ALL elements satisfy the predicate
    bool allPositive = std::all_of(numbers.begin(), numbers.end(),
        [](int x){ return x > 0; });

    if (allPositive) {
        std::cout << "All numbers are positive." << std::endl;
    } else {
        std::cout << "There is at least one non-positive number." << std::endl;
    }

    return 0;
}
```

# Lambda: join
```
# JS
const s = ["a", "b", "c"].join("-");

# Python
s = "-".join(["a", "b", "c"])
print(s)

# C++ (no direct join until C++23)
// C++
#include <iostream>      // std::cout
#include <vector>        // std::vector
#include <string>        // std::string
#include <sstream>       // optional if using stringstream

int main() {
    // Example input
    std::vector<std::string> vec = {"a", "b", "c"};

    // Manual join (C++ <23)
    std::string s;
    for (auto& x : vec) {
        if (!s.empty()) s += "-";       // add separator between elements
        s += x;                         // append element
    }

    // for (auto it = vec.begin(); it != vec.end(); ++it) {
    //     if (it != vec.begin()) s += "-";  // add separator
    //     s += *it;
    // }
    
    // std::ostringstream oss;
    // for (size_t i = 0; i < vec.size(); ++i) {
    //     if (i != 0) oss << "-";
    //     oss << vec[i];
    // }
    // std::string s = oss.str();

    std::cout << "Joined string: " << s << std::endl;

    return 0;
}
```

# Lambda: sort
```
# JS
numbers = [1,2,3,4];                                                    numbers = Array(1, 2, 3, 4);
numbers.sort((a,b) => a - b);

# Python
numbers = [1,2,3,4]
numbers.sort()
print(numbers)

# C++
#include <iostream>      // std::cout
#include <vector>        // std::vector
#include <algorithm>     // std::sort

int main() {
    std::vector<int> numbers = {1, 2, 3, 4};

    // C++ (std::sort)
    // Sorts elements in ascending order
    std::sort(numbers.begin(), numbers.end());

    for (int x : numbers) {
        std::cout << x << " ";
    }
    std::cout << std::endl;

    // Optional: sort in descending order using a lambda
    std::sort(numbers.begin(), numbers.end(),
        [](int a, int b){ return a > b; });

    std::cout << "Descending: ";
    for (int x : numbers) {
        std::cout << x << " ";
    }
    std::cout << std::endl;

    return 0;
}
```

## Back to README.md
[BACK](../README.md)