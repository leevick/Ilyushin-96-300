// import "./center.jpg" as CentralPanelBackgroud;

import { Component, React } from "react"
import center_upper_texture from "./center_upper_texture.jpg"


const b = 17.8
const a = -10
const c = -170
const ticks = Array.from(Array(71)).map((_, i) => (i * 10 + 100))

const angles = ticks.map((t, i) => Math.sqrt(t - a) * b + c)

export class US2 extends Component {

    constructor(props) {
        super(props)
        this.width = 800
        this.height = 800
        this.left = -400
        this.top = -400
    }

    render() {
        return <g id="US2" viewBox={`${this.left} ${this.top} ${this.width} ${this.height}`}>
            {/* <image x={-400} y={-400} width={800} height={800} href={us2} /> */}
            <circle r={400} x={0} y={0}></circle>
            <circle r={370} x={0} y={0}></circle>
            <text stroke="white" fill="white" x={-125} y={-60} fontSize={50} letterSpacing={-3} textLength={250} lengthAdjust="spacingAndGlyphs" fontFamily="lenya69">СКОРОСТЬ</text>
            {
                angles.map((a, i) => {
                    const tick = ticks[i]
                    if (tick % 100 === 0) {
                        return <text fontWeight={"bold"} transform={`translate(${Math.sin(a / 180 * Math.PI) * 240},${-Math.cos(a / 180 * Math.PI) * 240 + 10})`} dominantBaseline={"middle"} textAnchor="middle" stroke="white" fill="white" x={0} y={0} fontSize={100} fontFamily="lenya69">{tick / 100}</text>
                    } else {
                        return null
                    }

                })
            }

            {
                angles.map((a, i) => {

                    const tick = ticks[i]
                    if (tick % 100 === 0) {
                        return <rect x={0} y={0} width={10} height={60} transform={`translate(-5,-340) rotate(${a},5,340)`} fill="white" stroke="white"></rect>
                    } else if (tick % 50 === 0) {
                        return <rect x={0} y={0} width={5} height={60} transform={`translate(-5,-340) rotate(${a},5,340)`} fill="white" stroke="white"></rect>
                    } else {
                        return <rect x={0} y={0} width={5} height={30} transform={`translate(-5,-340) rotate(${a},5,340)`} fill="white" stroke="white"></rect>
                    }
                })
            }
        </g>
    }
}

export class RMIFace extends Component {
    constructor(props) {
        super(props)
        this.width = 740
        this.height = 740
        this.top = -370
        this.left = -370
    }

    render() {
        return <g id="RMIFace" viewBox={`${this.left} ${this.top} ${this.width} ${this.height}`}>
            <circle x={0} y={0} r={370} fillOpacity={0.5}></circle>
        </g>
    }

}
export class RMI extends Component {
    constructor(props) {
        super(props)
        this.width = 800
        this.height = 1150
        this.left = -this.width / 2
        this.top = -this.height / 2 - 100
    }

    render() {
        return <g id="RMI" viewBox={`${this.left} ${this.top} ${this.width} ${this.height}`}>
            <rect x={-this.width / 2} y={-this.height / 2 - 100} width={this.width} height={this.height} fill="rgb(101,139,148)" fillOpacity={0.5}></rect>
            <text stroke="white" fill="white" x={-210} y={410} fontSize={50} letterSpacing={-3} textLength={130} lengthAdjust="spacingAndGlyphs" fontWeight={"bold"} fontFamily="lenya69">APK</text>
            <text stroke="white" fill="white" x={210 - 130} y={410} fontSize={50} letterSpacing={-3} textLength={130} lengthAdjust="spacingAndGlyphs" fontWeight={"bold"} fontFamily="lenya69">APK</text>
            <text stroke="white" fill="white" x={- 395} y={135} fontSize={70} fontWeight={"bold"} fontFamily="lenya69">V</text>
            <text stroke="white" fill="white" x={- 395} y={185} fontSize={70} fontWeight={"bold"} fontFamily="lenya69">O</text>
            <text stroke="white" fill="white" x={- 395} y={235} fontSize={70} fontWeight={"bold"} fontFamily="lenya69">R</text>
            <text stroke="white" fill="white" x={390 - 35} y={135} fontSize={70} fontWeight={"bold"} fontFamily="lenya69">V</text>
            <text stroke="white" fill="white" x={390 - 35} y={185} fontSize={70} fontWeight={"bold"} fontFamily="lenya69">O</text>
            <text stroke="white" fill="white" x={390 - 35} y={235} fontSize={70} fontWeight={"bold"} fontFamily="lenya69">R</text>
            <text stroke="orange" textAnchor="middle" fill="orange" x={-160} y={-600} fontSize={60} letterSpacing={-3} textLength={70} lengthAdjust="spacingAndGlyphs" fontWeight={"bold"} fontFamily="lenya69">Д1</text>
            <text stroke="green" textAnchor="middle" fill="green" x={160} y={-600} fontSize={60} letterSpacing={-3} textLength={70} lengthAdjust="spacingAndGlyphs" fontWeight={"bold"} fontFamily="lenya69">Д2</text>
            <RMIFace></RMIFace>
        </g>
    }
}


export default class CentralPanel extends Component {

    constructor(props) {
        super(props)
        this.scale = 2.2
        this.width = this.scale * 1742
        this.height = this.scale * 918
        this.left = 0
        this.top = 0

        this.vbm_w = 800
        this.vbm_c = 5
        this.sig_w = 295
        this.sig_h = 165
        this.rmi_w = 800
        this.rmi_h = 1150
        this.stab_w = 300
        this.stab_h = 670
    }

    render() {
        return <g id="CentralPanel" viewBox={`${this.left} ${this.top} ${this.width} ${this.height}`}>
            <image x={0} y={0} width={1742 * this.scale} height={918 * this.scale} href={center_upper_texture} />
            {/* <circle name="us2" cx={512.5} cy={662.5} r={400} fill={"white"} fillOpacity={0.5} ></circle> */}

            <g transform="translate(512.5,662.5)">
                <US2></US2>
            </g>


            <g name="vp">
                <circle name="" cx={2465} cy={1500} r={400} fill={"white"} fillOpacity={1.0} ></circle>
            </g>
            <rect x={2065} y={250} width={this.vbm_w} height={this.vbm_w} fillOpacity={0.8}></rect>
            <rect x={820} y={1330} width={this.sig_w * 4} height={this.sig_h * 4} fillOpacity={1.0}></rect>
            <rect x={3225} y={1500} width={this.sig_w * 2} height={this.sig_h * 3} fillOpacity={1.0}></rect>
            {/* <circle cx={2465} cy={1500} r={400} fill={"white"} fillOpacity={1.0} ></circle> */}
            <g name="rmi" transform="translate(3335,950)">
                <RMI></RMI>
            </g>
            <g name="stab_disp" transform="translate(553,1545)">
                <rect width={this.stab_w} height={this.stab_h} x={-this.stab_w / 2} y={-this.stab_h / 2}></rect>
            </g>
            <g name="stab_sig" transform="translate(205,1545)">
                <rect width={this.sig_w} height={2 * this.sig_h} x={-this.sig_w / 2} y={-this.sig_h}></rect>
            </g>
        </g>
    }
}