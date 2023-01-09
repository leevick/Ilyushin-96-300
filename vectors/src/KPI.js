import { Component } from "react"
import kpi from "./kpi.jpg"


export default class KPI extends Component {

    constructor(props) {
        super(props)
        this.width = 1600
        this.height = 1600
        this.left = -800
        this.top = -800

        this.ahWidth = 730
        this.ahHeight = 850
        this.ahY = -145
        this.ahX = -12
        this.ahR = 75


    }
    render() {
        return <g id="KPI" viewBox={`${this.left} ${this.top} ${this.width} ${this.height}`}>
            <image x={-800} y={-800} width={1600} height={1600} href={kpi}></image>
            {/* <rect x={-800} y={-800} width={1600} height={1600} fill="black"></rect> */}
            <path d={`M -800 -800 l 0 1600 l 1600 0 l 0 -1600 Z M ${-this.ahWidth / 2 + this.ahX} ${-this.ahHeight / 2 + this.ahR + this.ahY} Z`} fill="black"></path>
            <rect rx={this.ahR} ry={this.ahR} x={-this.ahWidth / 2 + this.ahX} y={-this.ahHeight / 2 + this.ahY}
                width={this.ahWidth} height={this.ahHeight} fill="rgb(28,161,254)"></rect>
            {/* <rect x={-this.ahWidth / 2} y={-this.ahWidth / 2}
                width={this.ahWidth} height={this.ahWidth} fill="rgb(128,55,43)"></rect> */}
        </g>
    }
}