#include <iostream>
#include <vector>
#include <time.h>
#include <chrono>

using namespace std;
using namespace std::chrono;

void print_array(vector<int> numbers);
void quicksort(vector<int> &array, int left_index, int right_index);
int partition(vector<int> &array, int left_index, int right_index);
void merge_sort(vector<int> &array, int left_index, int right_index);
void merge(vector<int> &array, int left_index, int border, int right_index);
void insertion_sort(vector<int> &array, int left_index, int right_index);
void merge_insertion_sort(vector<int> &array, int left_index, int right_index, int k);
void quick_insertion_sort(vector<int> &array, int left_index, int right_index, int k);
nanoseconds define_min_k_index(vector<nanoseconds> times, int &index_k);

void calculate_magic_numbers(int num_arrays, int array_size, int max_k, int &min_k_merge_insertion, int &min_k_quick_insertion);
vector<vector<int>> generate_array(int size, int num_arrays, int min_num, int max_num);

void test_quicksort();
void test_insertion_sort();
void test_merge_sort();
void test_merge_insertion_sort(int k);
void test_quick_insertion_sort(int k);

int main()
{
    // doing some tests
    test_quicksort();
    test_insertion_sort();
    test_merge_sort();

    srand(time(NULL));
    int min_k_merge_insertion;
    int min_k_quick_insertion;
    calculate_magic_numbers(100, 10000, 100, min_k_merge_insertion, min_k_quick_insertion);

    test_merge_insertion_sort(min_k_merge_insertion);
    test_quick_insertion_sort(min_k_quick_insertion);
    
}

void print_array(vector<int> numbers)
{
    for (int i = 0; i < numbers.size(); i++)
    {
        cout << numbers[i] << " ";
    }
    cout << endl;
}

void quicksort(vector<int> &array, int left_index, int right_index)
{
    if (left_index < right_index)
    {
        int q = partition(array, left_index, right_index);
        quicksort(array, left_index, q);
        quicksort(array, q + 1, right_index);
    }
}

int partition(vector<int> &array, int left_index, int right_index)
{
    int pivot = array[(right_index + left_index) / 2];
    int i = left_index - 1;
    int j = right_index + 1;
    
    while(true)
    {
        do
        {
            i++;
        } while (array[i] < pivot);

        do
        {
            j--;
        } while (array[j] > pivot);
        
        if (i < j)
        {
            std::swap(array[i], array[j]);
        }
        else
        {
            return j;
        }
        
    }
}

void merge_sort(vector<int> &array, int left_index, int right_index)
{
    if ((right_index - left_index) + 1 < 2)
    {
        return;
    }

    if (left_index < right_index)
    {
        // dividing into pieces
        int pivot = (left_index + right_index) / 2;
        merge_sort(array, left_index, pivot);
        merge_sort(array, pivot + 1, right_index);
        
        merge(array, left_index, pivot, right_index);
    }
}

void merge(vector<int> &array, int left_index, int pivot, int right_index)
{
    vector<int> temp_array;

    // copy elements in temp array in sorted order
    int i = left_index, j = pivot + 1;
    while (i <= pivot && j <= right_index)
    {
        if (array[i] < array[j])
        {
            temp_array.push_back(array[i]);
            i++;
        }
        else
        {
            temp_array.push_back(array[j]);
            j++;
        }
    }

    // deal with tales after first for loop
    while (i <= pivot)
    {
        temp_array.push_back(array[i]);
        i++;
    }

    while (j <= right_index)
    {
        temp_array.push_back(array[j]);
        j++;
    }

    for (int i = left_index, k = 0; i <= right_index; i++, k++)
    {
        array[i] = temp_array[k];
    }
}

void insertion_sort(vector<int> &array, int left_index, int right_index)
{
    for (int i = left_index + 1; i <= right_index; i++) // n - 1
    {
        int x = array[i]; // 2
        int j = i - 1; // 2
        while (j >= 0 && array[j] > x) // 4  worst: n | best: 1
        {
            array[j + 1] = array[j]; // 3
            j--; // 1
        } // worst: 8n | best: 8
        array[j + 1] = x; // 2
    }
} // worst: 48n * (n - 1) | best: 48 * (n - 1)

void calculate_magic_numbers(int num_arrays, int array_size, int max_k, int &min_k_merge_insertion, int &min_k_quick_insertion)
{
    vector<nanoseconds> time_merge_insertion_vector;
    vector<int> k_merge_insertion;
    int k_merge_insertion_index = 0;

    vector<nanoseconds> time_quick_insertion_vector;
    vector<int> k_quick_insertion;
    int k_quick_insertion_index = 0;

    vector<vector<int>> random_arrays_1 = generate_array(array_size, num_arrays, 1, 1000);
    vector<vector<int>> random_arrays_2(random_arrays_1);

    cout << "MERGE_INSERTION SORT" << endl;
    for (int i = max_k; i >= 2; i--)
    {
        auto sum_time = std::chrono::nanoseconds::zero();
        for (int j = 0; j < num_arrays; j++)
        {
            auto start = high_resolution_clock::now();
            merge_insertion_sort(random_arrays_1[j], 0, array_size - 1, i);
            auto end = high_resolution_clock::now();
            auto duration = duration_cast<nanoseconds>(end - start);
            sum_time += duration;
        }
        
        sum_time /= num_arrays;
        time_merge_insertion_vector.push_back(sum_time);
        k_merge_insertion.push_back(i);
        cout << "Average time: " << sum_time.count() << " for k:" << i << endl;
    }

    cout << "-------------------" << endl;
    cout << "QUICK_INSERTION SORT" << endl;
    for (int i = max_k; i >= 2; i--)
    {
        auto sum_time = std::chrono::nanoseconds::zero();
        for (int j = 0; j < num_arrays; j++)
        {
            auto start = high_resolution_clock::now();
            quick_insertion_sort(random_arrays_2[j], 0, array_size - 1, i);
            auto end = high_resolution_clock::now();
            auto duration = duration_cast<nanoseconds>(end - start);
            sum_time += duration;
        }
        
        sum_time /= num_arrays;
        time_quick_insertion_vector.push_back(sum_time);
        k_quick_insertion.push_back(i);
        cout << "Average time: " << sum_time.count() << " for k:" << i << endl;
    }
    cout << "-------------------" << endl;

    int min_time_merge_insertion = define_min_k_index(time_merge_insertion_vector, k_merge_insertion_index).count();
    int min_time_quick_insertion = define_min_k_index(time_quick_insertion_vector, k_quick_insertion_index).count();
    min_k_merge_insertion = k_merge_insertion[k_merge_insertion_index];
    min_k_quick_insertion = k_quick_insertion[k_quick_insertion_index];

    cout << "Min time for merge insertion sort " << min_time_merge_insertion << " with k=" << min_k_merge_insertion << endl;
    cout << "Min time for quick insertion sort " << min_time_quick_insertion << " with k=" << min_k_quick_insertion << endl;
}

vector<vector<int>> generate_array(int size, int num_arrays, int min_num, int max_num)
{
    vector<vector<int>> random_arrays(num_arrays);

    for(int i = 0; i < num_arrays; i++)
    {
        for (int j = 0; j < size; j++)
        {
            int number = rand() % max_num + min_num;
            random_arrays[i].push_back(number);
        }
    }
    return random_arrays;
}

void merge_insertion_sort(vector<int> &array, int left_index, int right_index, int k)
{
    if ((right_index - left_index) + 1 <= k)
    {
        insertion_sort(array, left_index, right_index);
    }
    else
    {
        if ((right_index - left_index) + 1 < 2)
        {
            return;
        }
        if (left_index < right_index)
        {
            // dividing into pieces
            int pivot = (right_index + left_index) / 2;
            merge_insertion_sort(array, left_index, pivot, k);
            merge_insertion_sort(array, pivot, right_index, k);
            // merge_insertion_sort(array, pivot + 1, right_index, k); WTF?! IT'S NOT WORKING 
            
            merge(array, left_index, pivot, right_index);
        }
    }
}

void quick_insertion_sort(vector<int> &array, int left_index, int right_index, int k)
{
    if (right_index - left_index + 1 <= k)
    {
        insertion_sort(array, left_index, right_index);
        return;
    }

    if (left_index < right_index)
    {
        int q = partition(array, left_index, right_index);
        quick_insertion_sort(array, left_index, q, k);
        quick_insertion_sort(array, q + 1, right_index, k);
    }
}

nanoseconds define_min_k_index(vector<nanoseconds> times, int &index_k)
{
    auto min = times[0];
    for (int i = 0; i < times.size(); i++)
    {
        if (min >= times[i])
        {
            min = times[i];
            index_k = i;
        }
    }

    return min;
}

void test_quicksort()
{
    vector<int> numbers{23, 23, 4443, 25, 43, 8, 11, 7, 65, 83, 34};
    quicksort(numbers, 0, numbers.size() - 1);
    vector<int> expected{7, 8, 11, 23, 23, 25, 34, 43, 65, 83, 4443};
    bool test_bool = std::equal(numbers.begin(), numbers.end(), expected.begin());
    if (test_bool)
    {
        cout << "quicksort is working correctly" << endl;
        cout << "------------------------------" << endl;
    }
}

void test_insertion_sort()
{
    vector<int> numbers{23, 23, 4443, 25, 43, 8, 11, 7, 65, 83, 34};
    insertion_sort(numbers, 0, numbers.size() - 1);
    vector<int> expected{7, 8, 11, 23, 23, 25, 34, 43, 65, 83, 4443};
    bool test_bool = std::equal(numbers.begin(), numbers.end(), expected.begin());
    if (test_bool)
    {
        cout << "insertion_sort is working correctly" << endl;
        cout << "------------------------------" << endl;
    }
}

void test_merge_sort()
{
    vector<int> numbers{23, 23, 4443, 25, 43, 8, 11, 7, 65, 83, 34};
    merge_sort(numbers, 0, numbers.size() - 1);
    vector<int> expected{7, 8, 11, 23, 23, 25, 34, 43, 65, 83, 4443};
    bool test_bool = std::equal(numbers.begin(), numbers.end(), expected.begin());
    if (test_bool)
    {
        cout << "merge_sort is working correctly" << endl;
        cout << "------------------------------" << endl;
    }
}

void test_merge_insertion_sort(int k)
{
    vector<int> numbers{23, 23, 4443, 25, 43, 8, 11, 7, 65, 83, 34};
    merge_insertion_sort(numbers, 0, numbers.size() - 1, k);
    vector<int> expected{7, 8, 11, 23, 23, 25, 34, 43, 65, 83, 4443};
    bool test_bool = std::equal(numbers.begin(), numbers.end(), expected.begin());
    if (test_bool)
    {
        cout << "merge_insertion_sort is working correctly" << endl;
        cout << "------------------------------" << endl;
    }
}

void test_quick_insertion_sort(int k)
{
    vector<int> numbers{23, 23, 4443, 25, 43, 8, 11, 7, 65, 83, 34};
    quick_insertion_sort(numbers, 0, numbers.size() - 1, k);
    vector<int> expected{7, 8, 11, 23, 23, 25, 34, 43, 65, 83, 4443};
    bool test_bool = std::equal(numbers.begin(), numbers.end(), expected.begin());
    if (test_bool)
    {
        cout << "quick_insertion_sort is working correctly" << endl;
        cout << "------------------------------" << endl;
    }
}