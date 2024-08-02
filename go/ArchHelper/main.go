package main

import (
	"fmt"
	"os"
	"os/exec"
)

func runCmd(name string, arg ...string) {
	cmd := exec.Command(name, arg...)
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr
	err := cmd.Run()
	if err != nil {
		fmt.Printf("Error: %v\n", err)
	}
}

func clearScreen() {
	fmt.Print("\033[H\033[2J")
}

func main() {
	clearScreen()

	println("   ___,              _        ,          _                 ")
	println("  /   |             | |      /|   |     | |                ")
	println(" |    |   ,_    __  | |       |___|  _  | |   _   _   ,_   ")
	println(" |    |  /  |  /    |/ \\      |   |\\|/  |/  |/ \\_|/  /  |  ")
	println("  \\__/\\_/   |_/\\___/|   |_/   |   |/|__/|__/|__/ |__/   |_/")
	println("                                           /|              ")
	println("                                           \\|              ")

	fmt.Println("Welcome to the Arch Helper! Nice to meet you :)\nWhat do you want me to help you with?\n0 - Exit\n1 - Install a package\n2 - Run neofetch")
	var answer string
	fmt.Scanln(&answer)
	clearScreen()
	switch answer {
	case "0":
		fmt.Println("Bye!")
	case "1":
		fmt.Println("What package do you want me to install? Please prepare your root password too.")
		var packageName string
		fmt.Scanln(&packageName)
		clearScreen()
		runCmd("sudo", "pacman", "-S", "--noconfirm", packageName)
	case "2":
		clearScreen()
		runCmd("neofetch")
	default:
		fmt.Println("Invalid option. Please try again.")
	}
}
