import matplotlib.pyplot as plt

from benchmark.benchtests import test_algos_with_data_generator
from generator.first_generator import first_matrix_generator
from generator.second_generator import second_generator_matrix
from generator.target_calcs import target_for_first, target_for_second
from generator.test_cases import TEST_CASE_1

algo_results, rows_number_in_tests = test_algos_with_data_generator(first_matrix_generator,
                                                                    target_for_first,
                                                                    TEST_CASE_1,
                                                                    debug=True)


def hardcore_main():
    fig, ax = plt.subplots()
    ax.set_xlabel("Количестов строк M (столбцы=8192)")
    ax.set_ylabel("Время (мкс) ln")
    for algo_name, result in algo_results.items():
        plt.plot(rows_number_in_tests, result, label=algo_name, lw=5, mec='b', mew=2, ms=10)
    plt.legend()
    plt.semilogy()
    plt.show()


hardcore_main()
