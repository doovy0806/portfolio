/**
 * Created by Hanmo on 2017-09-07.
 */
/*
 * Name: ±¸ÇÑ¸ð Han Mo Ku
 * Student ID: 2014121136
 */

/*
 * Do not import anything
 */

public class Sorter {

    public Sorter() {
        /*
         * Constructor for our sorter
         * In this assignment you do not have to implement anything here
         * so just leave this method blank
         */
    }

    public int[] ascending(int[] input) {
        /*
         * ascending
         *
         * input - array of ints of length at least 0
         *
         * return the input array in ascending order
         */

        int lengthOfArray = input.length;
        int min = 0;
        int indexMin = 0;
        int temp = 0;
        int i = 0;
        for (; i < lengthOfArray; i++) {
            temp = input[i];
            min = input[i];
            indexMin = i;
            for (int j = i; j < lengthOfArray; j++) {
                if (min > input[j]) {
                    min = input[j];
                    indexMin = j;
                }
            }

            input[i] = min;
            input[indexMin] = temp;
        }

        return input;
    }

    public int[] descending(int[] input) {
        /*
         * descending
         *
         * input - array of ints of length at least 0
         *
         * return the input array in descending order
         */
        int lengthOfArray = input.length;
        int max = 0;
        int indexMax = 0;
        int temp = 0;
        int i = 0;
        for (; i < lengthOfArray; i++) {
            temp = input[i];
            max = input[i];
            indexMax = i;
            for (int j = i; j < lengthOfArray; j++) {
                if (max < input[j]) {
                    max = input[j];
                    indexMax = j;
                }
            }

        input[i] = max;
        input[indexMax] = temp;
        }
        return input;
    }
}
