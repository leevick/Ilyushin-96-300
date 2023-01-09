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

        const topBarSemiWidth = 540
        const topBarHeight = 120
        const sideBarSemiHeight = 400

        return <g id="KPI" viewBox={`${this.left} ${this.top} ${this.width} ${this.height}`}>
            <image x={-800} y={-800} width={1600} height={1600} href={kpi}></image>
            <path d={`M -800 -800 l 0 1600 l 1600 0 l 0 -1600 Z M ${-this.ahWidth / 2 + this.ahX} ${-this.ahHeight / 2 + this.ahR + this.ahY} a ${this.ahR} ${this.ahR} 0 0 1 ${this.ahR} ${-this.ahR} l ${this.ahWidth - 2 * this.ahR} 0 a ${this.ahR} ${this.ahR} 0 0 1 ${this.ahR} ${this.ahR} l 0 ${this.ahHeight - 2 * this.ahR} a ${this.ahR} ${this.ahR} 0 0 1 ${-this.ahR} ${this.ahR} l ${-this.ahWidth + 2 * this.ahR} 0 a ${this.ahR} ${this.ahR} 0 0 1 ${-this.ahR} ${-this.ahR} Z`} fill="black" stroke="yellow" strokeWidth={10} strokeOpacity={0}></path>
            {/* <rect rx={this.ahR} ry={this.ahR} x={-this.ahWidth / 2 + this.ahX} y={-this.ahHeight / 2 + this.ahY}
                width={this.ahWidth} height={this.ahHeight} fill="rgb(28,161,254)"></rect> */}
            {/* <rect x={-this.ahWidth / 2} y={-this.ahWidth / 2}
                width={this.ahWidth} height={this.ahWidth} fill="rgb(128,55,43)"></rect> */}
            <g transform={`translate(${this.ahX},${this.ahY})`}>
                <rect fill="grey" x={-topBarSemiWidth} y={-600} width={2 * topBarSemiWidth} height={topBarHeight} fillOpacity={1}></rect>
                {
                    [1, 2].map((i) => <line y1={-600} y2={-600 + topBarHeight} x1={-topBarSemiWidth + i * 360} x2={-topBarSemiWidth + i * 360} stroke="white" strokeWidth={5}></line>)
                }
                {
                    [1, 2].map((i) => <line y1={-600} y2={-600 + topBarHeight} x1={-topBarSemiWidth + i * 360} x2={-topBarSemiWidth + i * 360} stroke="white" strokeWidth={5}></line>)
                }
                {
                    [0, 1, 3, 4].map((i) =>
                        <circle cx={-190 + i * 95} cy={446} r={12} strokeWidth={6} stroke="white" fill="none"></circle>
                    )
                }
                <rect x={-755} y={-sideBarSemiHeight} height={2 * sideBarSemiHeight} width={120} fill="grey"></rect>
                <rect fillOpacity={1} x={-600} y={-sideBarSemiHeight} height={2 * sideBarSemiHeight} width={180} fill="grey"></rect>
                <rect fillOpacity={1} x={420} y={-sideBarSemiHeight} height={2 * sideBarSemiHeight} width={210} fill="grey"></rect>
            </g>
        </g>
    }
}