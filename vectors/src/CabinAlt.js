import { Component } from "react";
import CabinAltimeter from "./cabin_altimeter.png"

export default class CabinAlt extends Component {
    constructor(props) {
        super(props)
        this.width = 800
        this.height = 800
        this.left = -400
        this.top = -400
    }

    render() {

        const UVPD_Main = [36, 65, 95, 125, 152, 180, 210, 237, 267, 297, 325]
        const UVPDMainNumberAngle = [28, 95, 152, 210, 267, 340]
        const UVPDMainNumberRadius = [350, 350, 350, 350, 350, 350]

        return <g id={"CabinAlt"} viewBox={`${this.left} ${this.top} ${this.width} ${this.height}`}>
            <image x={-370} y={-370} href={CabinAltimeter}></image>
            <circle r={370} fillOpacity={1} fill="hsl(211,49%,33%)" stroke="none"></circle>
            <circle r={250} fillOpacity={1} fill="black" stroke="none"></circle>


            {
                UVPD_Main.map((a, i) => (
                    <line x1={-Math.sin(Math.PI / 180 * a) * 365}
                        y1={Math.cos(Math.PI / 180 * a) * 365}
                        x2={-Math.sin(Math.PI / 180 * a) * 320}
                        y2={Math.cos(Math.PI / 180 * a) * 320}
                        strokeWidth={10} stroke="white" strokeLinecap="round"></line>
                ))
            }


            {
                UVPD_Main.map((a, i) => (
                    i === UVPD_Main.length - 1 ? null :
                        Array.from({ length: 5 }, (_, j) =>
                            <line x1={-Math.sin(Math.PI / 180 * a + Math.PI / 180 * (UVPD_Main[i + 1] - UVPD_Main[i]) / 5 * j) * 367.5}
                                y1={Math.cos(Math.PI / 180 * a + Math.PI / 180 * (UVPD_Main[i + 1] - UVPD_Main[i]) / 5 * j) * 367.5}
                                x2={-Math.sin(Math.PI / 180 * a + Math.PI / 180 * (UVPD_Main[i + 1] - UVPD_Main[i]) / 5 * j) * 335}
                                y2={Math.cos(Math.PI / 180 * a + Math.PI / 180 * (UVPD_Main[i + 1] - UVPD_Main[i]) / 5 * j) * 335}
                                strokeWidth={5} stroke="white" strokeLinecap="round"></line>
                        )
                ))
            }

            {
                UVPDMainNumberAngle.map((a, i) => <text stroke="white" textLength="50" lengthAdjust={"spacingAndGlyphs"} letterSpacing={-3} fill="white" dominantBaseline="middle" textanchor="middle"
                    x={-Math.sin(Math.PI / 180 * a) * 310}
                    y={Math.cos(Math.PI / 180 * a) * 300} fontFamily="lenya69" fontSize={100}>{i}</text>
                )
            }

        </g>
    }

}