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
        const UVPDMainNumberAngle = [28, 95, 150, 200, 267, 340]
        const UVPDMainNumberRadius = [310, 310, 295, 250, 250, 310]
        const InnerMainTicks = [-50, -14, 22, 50, 88, 118, 150, 185, 210]


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
                    x={-Math.sin(Math.PI / 180 * a) * UVPDMainNumberRadius[i]}
                    y={Math.cos(Math.PI / 180 * a) * UVPDMainNumberRadius[i]} fontFamily="lenya69" fontSize={100}>{i}</text>
                )
            }

            {
                InnerMainTicks.map((a, i) => (
                    <line x1={Math.cos(Math.PI / 180 * a) * 247.5}
                        y1={Math.sin(Math.PI / 180 * a) * 247.5}
                        x2={Math.cos(Math.PI / 180 * a) * 210}
                        y2={Math.sin(Math.PI / 180 * a) * 210}
                        strokeWidth={10} stroke="white" strokeLinecap="round"></line>
                ))
            }

            <path stroke="white" strokeWidth={5} fill="none" d={`M ${Math.cos(Math.PI / 180 * -50) * 250} ${Math.sin(Math.PI / 180 * -50) * 250} A 250 250 0 1 1 ${-Math.cos(Math.PI / 180 * -50) * 250} ${Math.sin(Math.PI / 180 * -50) * 250}`}></path>


            <text fontFamily="lenya69" stroke="white" lengthAdjust={"spacingAndGlyphs"} letterSpacing={0} fill="white" dominantBaseline="middle" textanchor="middle"
                x={-60}
                y={-230}
                fontSize={30}
                textLength={120}
            >ПЕРЕПАД</text>

            <text fontFamily="lenya69" stroke="white" lengthAdjust={"spacingAndGlyphs"} letterSpacing={0} fill="white" dominantBaseline="middle" textanchor="middle"
                x={-60}
                y={-230 + 30}
                fontSize={30}
                textLength={120}
            >ДАВЛЕНИИ</text>


            <text fontFamily="lenya69" stroke="white" lengthAdjust={"spacingAndGlyphs"} letterSpacing={0} fill="white" dominantBaseline="middle" textanchor="middle"
                x={-70}
                y={310}
                fontSize={30}
                textLength={120}
            >В КАБИНА</text>

            <text fontFamily="lenya69" stroke="white" lengthAdjust={"spacingAndGlyphs"} letterSpacing={0} fill="white" dominantBaseline="middle" textanchor="middle"
                x={-60}
                y={280}
                fontSize={30}
                textLength={100}
            >ВЫСОТА</text>


        </g>
    }

}