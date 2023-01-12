import { Component } from "react"
import kpi from "./kpi.jpg"


export default class KPI extends Component {

    constructor(props) {
        super(props)
        this.width = 1600
        this.height = 1600
        this.left = -800
        this.top = -800
        this.state = {
            roll: 0,
            pitch: 0,
            heading: 40,
            track: 0,
            mach: 0,
            ias: 0,
            mach_tgt: 0,
            ias_tgt: 0,
            aoa: 0
        }



    }

    componentDidMount() {
        setInterval(() => {
            this.setState(prev => ({
                ...prev,
                roll: prev.roll + (Math.random() * 2 - 1),
                pitch: prev.pitch + (Math.random() * 2 - 1),
                heading: (prev.heading + Math.random() * 2 - 1) % 360
            }))
        }, 20);
    }

    render() {

        const pitch = this.state.pitch
        const roll = this.state.roll
        const pitchY = 750 * Math.sin(pitch / 180 * Math.PI)
        const maxAoA = 15
        const AoA = 4.5

        const ahWidth = 730
        const ahHeight = 850
        const ahY = -145
        const ahX = -12
        const ahR = 75
        const topBarSemiWidth = 540
        const topBarHeight = 120
        const sideBarSemiHeight = 400
        const rollTickColors = ["red", "red", "yellow", "white", "white", "white", "white", "white", "yellow", "red", "red"]
        const rollTickLenght = [45, 45, 45, 30, 30, 45, 30, 30, 45, 45, 45]
        const slideBarSemiWidth = 165
        const slideBarHeight = 50
        const pitchSemiWidth = [150, 30, 150, 30, 150, 30, 80, 20, 40, 20, 20, 40, 20, 80, 30, 150, 30, 150, 30, 150]
        const pitchText = ["40", "", "30", "", "20", "", "10", "", "", "", "", "", "", "10", "", "20", "", "30", "", "40"]

        return <g id="KPI" viewBox={`${this.left} ${this.top} ${this.width} ${this.height}`}>
            <image x={-800} y={-800} width={1600} height={1600} href={kpi}></image>

            <g transform={`translate(${ahX},${ahY})`}>
                <g transform={`translate(0,${pitchY}) rotate(${roll},0,${-pitchY})`}>
                    <rect fillOpacity={1} x={-800} y={-800} width={1600} height={800} fill="rgb(28,161,254)"></rect>
                    <rect fillOpacity={1} x={-800} y={0} width={1600} height={800} fill="rgb(128,55,43)"></rect>
                    {
                        [-40, -35, -30, -25, -20, -15, -10, -7.5, -5, -2.5, 2.5, 5.0, 7.5, 10, 15, 20, 25, 30, 35, 40].map((a, i) => {
                            const tickY = 750 * Math.sin(a / 180 * Math.PI)
                            if (Math.abs(pitchY + tickY) > 350)
                                return null
                            else return <g>
                                <line x1={-pitchSemiWidth[i]} x2={pitchSemiWidth[i]} y1={tickY} y2={tickY} stroke="white" strokeWidth={5}></line>
                                <text y={750 * Math.sin(a / 180 * Math.PI)} x={pitchSemiWidth[i] + 10} dominantBaseline="central" stroke="white" fill="white" fontSize={50} textLength={50} fontFamily="lenya69">{pitchText[i]}</text>
                                <text y={750 * Math.sin(a / 180 * Math.PI)} x={-pitchSemiWidth[i] - 60} dominantBaseline="central" stroke="white" fill="white" fontSize={50} textLength={50} fontFamily="lenya69">{pitchText[i]}</text>

                            </g>
                        })
                    }
                </g>
            </g>
            <g transform={`translate(${ahX},${ahY})`}>
                <g transform={`rotate(${roll})`}>
                    <path d="M 0 -420 l 15 30 l -15 30 l -15 -30 Z" stroke="white" strokeWidth={5} fill="none"></path>
                    <path d="M 0 380 l -18 -50 l 36 0 Z" fill="white"></path>
                </g>
            </g>

            <g transform={`translate(${ahX},${ahY})`}>
                <circle rx={0} ry={0} r={20} strokeWidth={10} stroke="white" fill="none"></circle>
                {
                    [-60, -45, -30, -20, -10, 0, 10, 20, 30, 45, 60].map((a, i) => <line strokeOpacity={1} x1={0} x2={0} y1={380} y2={380 + rollTickLenght[i]} stroke={rollTickColors[i]} strokeWidth={5} transform={`rotate(${a})`}></line>)
                }
                <path d="M -300 -5 l 210 0 l 0 40 l -10 0 l 0 -30 l -200 0 Z" stroke="white" strokeWidth={5} fill="none"></path>
                <path d="M 300 -5 l -210 0 l 0 40 l 10 0 l 0 -30 l 200 0 Z" stroke="white" strokeWidth={5} fill="none"></path>

            </g>

            <path d={`M -800 -800 l 0 1600 l 1600 0 l 0 -1600 Z M ${-ahWidth / 2 + ahX} ${-ahHeight / 2 + ahR + ahY} a ${ahR} ${ahR} 0 0 1 ${ahR} ${-ahR} l ${ahWidth - 2 * ahR} 0 a ${ahR} ${ahR} 0 0 1 ${ahR} ${ahR} l 0 ${ahHeight - 2 * ahR} a ${ahR} ${ahR} 0 0 1 ${-ahR} ${ahR} l ${-ahWidth + 2 * ahR} 0 a ${ahR} ${ahR} 0 0 1 ${-ahR} ${-ahR} Z`} fill="black" stroke="yellow" strokeWidth={10} strokeOpacity={0}></path>
            <g transform={`translate(${ahX},${ahY})`}>
                <path d="M 0 -425 l -14.433756729740644112728719512549 -25 l 28.867513459481288225457439025098 0 Z" stroke="white" strokeWidth={5} fill="none"></path>
                {/* Top bar */}
                <rect fill="grey" x={-topBarSemiWidth} y={-600} width={2 * topBarSemiWidth + 10} height={topBarHeight} fillOpacity={1}></rect>
                <text x={-topBarSemiWidth - 15} y={-600 + 10} dominantBaseline={"hanging"} textAnchor="end" fontFamily="lenya69" fill="rgb(0,255,0)" stroke="rgb(0,255,0)" strokeWidth={2} fontSize={60}>AT</text>
                <text x={-topBarSemiWidth + 50} y={-600 + 10} dominantBaseline={"hanging"} textAnchor="start" fontFamily="lenya69" fill="rgb(0,255,0)" stroke="rgb(0,255,0)" strokeWidth={2} fontSize={60}>ЧИСЛО M</text>
                <text x={-topBarSemiWidth + 350} y={-600 + 10} dominantBaseline={"hanging"} textAnchor="start" fontFamily="lenya69" fill="rgb(0,255,0)" stroke="rgb(0,255,0)" strokeWidth={2} fontSize={60}>ГОР НАВ</text>
                <text x={200} y={-600 + 10} dominantBaseline={"hanging"} textAnchor="start" fontFamily="lenya69" fill="rgb(0,255,0)" stroke="rgb(0,255,0)" strokeWidth={2} fontSize={60}>ВЫСОТА</text>
                <text x={topBarSemiWidth + 40} y={-600 + 10} dominantBaseline={"hanging"} textAnchor="start" fontFamily="lenya69" fill="rgb(0,255,0)" stroke="rgb(0,255,0)" strokeWidth={2} fontSize={60}>AП</text>
                <line y1={-600} y2={-600 + topBarHeight} x1={-topBarSemiWidth + 1 * 360 - 25} x2={-topBarSemiWidth + 1 * 360 - 25} stroke="white" strokeWidth={5}></line>
                <line y1={-600} y2={-600 + topBarHeight} x1={-topBarSemiWidth + 2 * 360} x2={-topBarSemiWidth + 2 * 360} stroke="white" strokeWidth={5}></line>

                <g transform="translate(0,446)">
                    <path fillOpacity={1} fill="rgb(255,0,255)" d="M 0 -15 l 30 15 l -30 15 l -30 -15 Z"></path>
                </g>
                {
                    [0, 1, 3, 4].map((i) =>
                        <circle cx={-190 + i * 95} cy={446} r={12} strokeWidth={6} stroke="white" fill="none"></circle>
                    )
                }
                {/* Angle of Attack*/}
                <rect x={-755} y={-sideBarSemiHeight} height={2 * sideBarSemiHeight} width={120} fill="grey"></rect>
                {
                    [-5, 0, 5, 10, 15, 20, 25].map((aoa, i) => <line x1={-635} x2={-680} y1={-aoa * 20 + 100} y2={-aoa * 20 + 100} stroke={aoa >= maxAoA ? "red" : "white"} strokeWidth={8}></line>)
                }
                <line x1={-635} x2={-615} y1={-maxAoA * 20 + 100} y2={-maxAoA * 20 + 100} stroke={"red"} strokeWidth={8}></line>
                {
                    [0, 10, 20].map((aoa, i) => <text textAnchor="end" dominantBaseline="central" fontFamily="lenya69" x={-695} y={-aoa * 20 + 100} fontSize={60} fill={aoa >= maxAoA ? "red" : "white"} stroke={aoa >= maxAoA ? "red" : "white"} strokeWidth={2}>{aoa}</text>)
                }
                {
                    [0, 5, 10, 15].map((baseAoA, i) =>
                        [1, 2, 3, 4].map((aoa, j) => <line x1={-635} x2={-655} y1={-(aoa + baseAoA) * 20 + 100} y2={-(aoa + baseAoA) * 20 + 100} stroke={(aoa + baseAoA) >= maxAoA ? "red" : "white"} strokeWidth={8}></line>)
                    )
                }
                <line x1={-635} x2={-635} y1={-404} y2={-(maxAoA) * 20 + 104} stroke="red" strokeWidth={8}></line>
                <line x1={-635} x2={-635} y1={400} y2={-(maxAoA) * 20 + 104} stroke="white" strokeWidth={8}></line>
                <g transform={`translate(${-655},${-AoA * 20 + 100})`}>
                    <path d="M 0 0 l -40 -20 l 0 40 Z" fill="rgb(0,255,0)"></path>
                </g>
                {/* Airspeed */}
                <rect fillOpacity={1} x={-600} y={-sideBarSemiHeight} height={2 * sideBarSemiHeight} width={180} fill="grey"></rect>
                <path fillOpacity={1} d="M -420 0 l -30 0 l -30 -40 l -140 0 l 0 80 l 140 0 l 30 -40" stroke="rgb(0,255,0)" strokeWidth={8}></path>
                <text textAnchor="middle" x={-510} y={-sideBarSemiHeight - 10} fontFamily="lenya69" fontSize={100} fill="rgb(0,0,255)">0.770</text>
                <text textAnchor="start" dominantBaseline="central" y={0} x={-610} fill="white" fontSize={100} fontFamily="lenya69">505</text>
                <text textAnchor="middle" dominantBaseline={"hanging"} x={-510} y={+sideBarSemiHeight + 20} fontFamily="lenya69" fontSize={60} textLength={150} stroke="white" fill="white">0.771</text>

                {/* Altitude */}
                <rect fillOpacity={1} x={420} y={-sideBarSemiHeight} height={2 * sideBarSemiHeight} width={210} fill="grey"></rect>
                <rect fillOpacity={1} x={-slideBarSemiWidth} y={475} height={slideBarHeight} width={2 * slideBarSemiWidth} fill="grey"></rect>
                <line stroke="white" strokeWidth={5} x1={-slideBarSemiWidth} x2={-slideBarSemiWidth} y1={475} y2={525}></line>
                <line stroke="white" strokeWidth={5} x1={slideBarSemiWidth} x2={slideBarSemiWidth} y1={475} y2={525}></line>
                <circle fill="rgb(0,255,0)" r={20} strokeWidth={6} cx={0} cy={500}></circle>
                <line stroke="white" strokeWidth={5} x1={0} x2={0} y1={425} y2={525}></line>

                {/* Compass */}
                <g transform="translate(0,1300)">
                    <g transform={`rotate(${-this.state.heading})`}>
                        <circle strokeWidth={5} fillOpacity={1} stroke="white" fill="grey" r={600} cy={0}></circle>
                        {
                            Array.from(Array(72)).map((_, i) => <g transform={`rotate(${i * 5})`}>
                                <line x1={0} x2={0} y1={-600} y2={i % 2 ? -575 : -560} stroke="white" strokeWidth={5}></line>
                                <text fill="white" stroke="white" x={0} y={-560} fontSize={60} fontFamily="lenya69" textAnchor="middle" dominantBaseline="hanging">{i % 6 ? "" : (i * 5 / 10).toFixed(0).padStart(2, "0")}</text>
                            </g>)
                        }
                    </g>
                    <path d="M 0 -600 l 0 -10 l 30 -30 l 50 0 l 0 -70 l -160 0 l 0 70 l 50 0 l 30 30" stroke="rgb(0,255,0)" strokeWidth={5} ></path>
                    <text fill="white" stroke="white" x={0} y={-600 - 75} fontSize={80} fontFamily="lenya69" textAnchor="middle" dominantBaseline="central">{Math.round(this.state.heading).toFixed(0).padStart(3, '0')}</text>
                </g>
            </g>
            <rect x={-800} y={770} width={1600} height={30} fillOpacity={1} fill="black"></rect>

            <path fill="grey" strokeWidth={5} d={`M 800 ${ahY - sideBarSemiHeight + 100} l -60 -100 l -105 0 l 0 220 l 70 90 l 0 180 l -70 90 l 0 220 l 105 0 l 60 -100 Z`}></path>
        </g>
    }
}