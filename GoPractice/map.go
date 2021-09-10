package main

import "fmt"

func main() {
	varName := map[string]int{
		"hi":    2,
		"hello": 5,
	}
	for key, value := range varName {
		fmt.Printf("key %s, value %d \n", key, value)
	}
}
