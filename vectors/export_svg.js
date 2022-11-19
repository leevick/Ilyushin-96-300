#!/usr/bin/node
import { parse } from 'node-html-parser'
import fs from 'fs'

const t = process.argv.slice(2)[0]

const html = fs.readFileSync("./build/index.html", 'utf-8')
const root = parse(html)

const fd = fs.openSync(`./build/${t}.svg`, "w+")
const svg = root.querySelector(`#${t}`).toString()
fs.writeSync(fd, '<?xml version="1.0" encoding="UTF-8"?>')
fs.writeSync(fd, svg)
fs.close(fd)
