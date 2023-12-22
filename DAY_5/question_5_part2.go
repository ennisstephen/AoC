package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

type Array struct {
	Values [][]int
}

func getNextNumber(arrays [][]int, seedNum int) int {
	for _, array := range arrays {
		if seedNum >= array[1] && seedNum <= array[1]+array[2] {
			amountToIncrease := seedNum - array[1]
			return array[0] + amountToIncrease
		}
	}
	return seedNum
}

func main() {
	var myArrays []Array

	content, err := ioutil.ReadFile("input.txt")
	if err != nil {
		fmt.Println("Error reading file:", err)
		return
	}

	splitByCategory := strings.Split(string(content), "\n\n")

	for _, line := range splitByCategory {
		var arrayOfNumbers [][]int
		words := strings.Split(line, "\n")
		for _, word := range words {
			nums := strings.Split(word, " ")
			var smallerArray []int
			for _, num := range nums {
				if val, err := strconv.Atoi(num); err == nil {
					smallerArray = append(smallerArray, val)
				}
			}
			if len(smallerArray) > 0 {
				arrayOfNumbers = append(arrayOfNumbers, smallerArray)
			}
		}
		myArrays = append(myArrays, Array{Values: arrayOfNumbers})
	}

	seeds := myArrays[0].Values[0]
	seedToSoilMap := myArrays[1].Values
	soilToFertilizerMap := myArrays[2].Values
	fertilizerToWaterMap := myArrays[3].Values
	waterToLightMap := myArrays[4].Values
	lightToTemperatureMap := myArrays[5].Values
	temperatureToHumidityMap := myArrays[6].Values
	humidityToLocationMap := myArrays[7].Values

	finalLocation := -1
	x := 0

	fmt.Println(seeds)
	for x < len(seeds) {
		for y := seeds[x]; y < seeds[x]+seeds[x+1]; y++ {
			location := getNextNumber(seedToSoilMap, y)
			location = getNextNumber(soilToFertilizerMap, location)
			location = getNextNumber(fertilizerToWaterMap, location)
			location = getNextNumber(waterToLightMap, location)
			location = getNextNumber(lightToTemperatureMap, location)
			location = getNextNumber(temperatureToHumidityMap, location)
			location = getNextNumber(humidityToLocationMap, location)
			if finalLocation == -1 {
				finalLocation = location
			} else if location < finalLocation {
				finalLocation = location
			}
		}
		x += 2
		if x >= len(seeds) {
			break
		}
	}

	fmt.Println(finalLocation)
}
