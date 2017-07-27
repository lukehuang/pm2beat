package main

import (
	"os"

	"github.com/elastic/beats/libbeat/beat"

	"github.com/maityneil001/pm2beat/beater"
)

func main() {
	err := beat.Run("pm2beat", "", beater.New)
	if err != nil {
		os.Exit(1)
	}
}
