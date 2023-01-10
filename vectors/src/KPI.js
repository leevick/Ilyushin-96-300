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
        const rollTickColors = ["red", "red", "yellow", "white", "white", "white", "white", "white", "yellow", "red", "red"]
        const rollTickLenght = [45, 45, 45, 30, 30, 45, 30, 30, 45, 45, 45]
        const slideBarSemiWidth = 165
        const slideBarHeight = 50
        const pitchSemiWidth = [30, 150, 30, 80, 20, 40, 20, 20, 40, 20, 80, 30, 150, 30]
        const pitchText = ["", "20", "", "10", "", "", "", "", "", "", "10", "", "20", ""]

        return <g id="KPI" viewBox={`${this.left} ${this.top} ${this.width} ${this.height}`}>
            <image x={-800} y={-800} width={1600} height={1600} href={kpi}></image>

            <g transform={`translate(${this.ahX},${this.ahY})`}>
                <g transform={`translate(0,35) rotate(13.5,0,-35)`}>
                    <rect fillOpacity={1} x={-800} y={-800} width={1600} height={800} fill="rgb(28,161,254)"></rect>
                    <rect fillOpacity={1} x={-800} y={0} width={1600} height={800} fill="rgb(128,55,43)"></rect>
                    {
                        [-25, -20, -15, -10, -7.5, -5, -2.5, 2.5, 5.0, 7.5, 10, 15, 20, 25].map((a, i) => <g>
                            <line x1={-pitchSemiWidth[i]} x2={pitchSemiWidth[i]} y1={750 * Math.sin(a / 180 * Math.PI)} y2={750 * Math.sin(a / 180 * Math.PI)} stroke="white" strokeWidth={5}></line>
                            <text y={750 * Math.sin(a / 180 * Math.PI)} x={pitchSemiWidth[i] + 10} dominantBaseline="central" stroke="white" fill="white" fontSize={50} textLength={50} fontFamily="lenya69">{pitchText[i]}</text>
                            <text y={750 * Math.sin(a / 180 * Math.PI)} x={-pitchSemiWidth[i] - 60} dominantBaseline="central" stroke="white" fill="white" fontSize={50} textLength={50} fontFamily="lenya69">{pitchText[i]}</text>

                        </g>)
                    }
                </g>
            </g>

            <g transform={`translate(${this.ahX},${this.ahY})`}>
                <circle rx={0} ry={0} r={20} strokeWidth={10} stroke="white" fill="none"></circle>
                {
                    [-60, -45, -30, -20, -10, 0, 10, 20, 30, 45, 60].map((a, i) => <line strokeOpacity={1} x1={0} x2={0} y1={380} y2={380 + rollTickLenght[i]} stroke={rollTickColors[i]} strokeWidth={5} transform={`rotate(${a})`}></line>)
                }
                <path d="M -300 -5 l 210 0 l 0 40 l -10 0 l 0 -30 l -200 0 Z" stroke="white" strokeWidth={5} fill="none"></path>
                <path d="M 300 -5 l -210 0 l 0 40 l 10 0 l 0 -30 l 200 0 Z" stroke="white" strokeWidth={5} fill="none"></path>

            </g>

            <path d={`M -800 -800 l 0 1600 l 1600 0 l 0 -1600 Z M ${-this.ahWidth / 2 + this.ahX} ${-this.ahHeight / 2 + this.ahR + this.ahY} a ${this.ahR} ${this.ahR} 0 0 1 ${this.ahR} ${-this.ahR} l ${this.ahWidth - 2 * this.ahR} 0 a ${this.ahR} ${this.ahR} 0 0 1 ${this.ahR} ${this.ahR} l 0 ${this.ahHeight - 2 * this.ahR} a ${this.ahR} ${this.ahR} 0 0 1 ${-this.ahR} ${this.ahR} l ${-this.ahWidth + 2 * this.ahR} 0 a ${this.ahR} ${this.ahR} 0 0 1 ${-this.ahR} ${-this.ahR} Z`} fill="black" stroke="yellow" strokeWidth={10} strokeOpacity={0}></path>
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
                <rect fillOpacity={1} x={-slideBarSemiWidth} y={475} height={slideBarHeight} width={2 * slideBarSemiWidth} fill="grey"></rect>
                <line stroke="white" strokeWidth={5} x1={-slideBarSemiWidth} x2={-slideBarSemiWidth} y1={475} y2={525}></line>
                <line stroke="white" strokeWidth={5} x1={slideBarSemiWidth} x2={slideBarSemiWidth} y1={475} y2={525}></line>
                <circle fill="rgb(0,255,0)" r={20} strokeWidth={6} cx={0} cy={500}></circle>
            </g>
            <path fill="grey" strokeWidth={5} d={`M 800 ${this.ahY - sideBarSemiHeight + 100} l -60 -100 l -105 0 l 0 220 l 70 90 l 0 180 l -70 90 l 0 220 l 105 0 l 60 -100 Z`}></path>
        </g>
    }
}