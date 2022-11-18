#!/usr/bin/node
import { parse } from 'node-html-parser';
import fs from 'fs'


const textures = ["us2"]


const html = fs.readFileSync("./build/index.html", 'utf-8')
const root = parse(html)

textures.map(t => {

    const fd = fs.openSync(`${t}.svg`, "w+")
    const svg = root.querySelector('#us2').toString()
    fs.writeSync(fd, '<?xml version="1.0" encoding="UTF-8"?>')
    fs.writeSync(fd, svg)
    fs.close(fd)

})
