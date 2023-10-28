
import { Component, React } from "react"
import blackNut from "./black_nut.png"

export class SPSH4 extends Component {
    constructor(props) {
        super(props)
        this.width = 650
        this.height = 650
        this.top = 0
        this.left = 0
        this.bevelWidth = 162.5
    }

    render() {
        return <g>
            <path d={`M ${this.bevelWidth} 0 
            l ${this.width - 2 * this.bevelWidth} 0 
            l ${this.bevelWidth} ${this.bevelWidth}
            l ${0} ${this.width - 2 * this.bevelWidth}
            l ${-this.bevelWidth} ${this.bevelWidth}
            l ${-this.width + 2 * this.bevelWidth} ${0}
            l ${-this.bevelWidth} ${-this.bevelWidth}
            l ${0} ${-this.width + 2 * this.bevelWidth}
            Z`} color={"black"} fill={"black"} stroke={"black"} strokeWidth={5} />
            <g id="SPSH4" viewBox="0 0 650 650">

                <path d="M 200 490 l 0 -130
                        c 0 -90 70 -190 100 -215 
                        c 15 -15 35 -15 50 0 
                        c 30 25 100 125 100 215
                        l 0 130
            " stroke="white" strokeWidth={5} fill="none"></path>
                <text letterSpacing={-3} textLength={150} lengthAdjust="spacingAndGlyphs" x={250} y={375} dominantBaseline="central" fontSize={50} fill="white" stroke="white" strokeWidth={0} fontFamily="lenya69">ШАССИ</text>
                <line x1={150} y1={490} x2={500} y2={490} strokeWidth={5} stroke="white"></line>
            </g>
            <g id="SPSH4NUTS" viewBox="0 0 650 650">
                <g transform="translate(45,325)">
                    <g transform={`rotate(${Math.random() * 360})`}>
                        <g transform="translate(-30,-30)">
                            <image href={blackNut} width={60} height={60}></image>
                        </g>
                    </g>
                </g>
                <g transform="translate(605,325)">
                    <g transform={`rotate(${Math.random() * 360})`}>
                        <g transform="translate(-30,-30)">
                            <image href={blackNut} width={60} height={60}></image>
                        </g>
                    </g>
                </g>
            </g>

            <circle cx={325} cy={95} r={30} fill="#00ff00"></circle>
            <circle cx={325} cy={530} r={30} fill="#00ff00"></circle>
            <circle cx={160} cy={455} r={30} fill="#00ff00"></circle>
            <circle cx={490} cy={455} r={30} fill="#00ff00"></circle>
            <circle cx={240} cy={325} r={30} fill="#ffff00"></circle>
            <circle cx={410} cy={325} r={30} fill="#ffff00"></circle>
            <circle cx={325} cy={425} r={30} fill="#ffff00"></circle>
            <circle cx={325} cy={205} r={30} fill="#ffff00"></circle>
        </g>
    }
}