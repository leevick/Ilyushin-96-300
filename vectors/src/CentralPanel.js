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
                        return <rect x={0} y={0} width={5} height={60} transform={`translate(-2.5,-340) rotate(${a},2.5,340)`} fill="white" stroke="white"></rect>
                    } else {
                        return <rect x={0} y={0} width={5} height={30} transform={`translate(-2.5,-340) rotate(${a},2.5,340)`} fill="white" stroke="white"></rect>
                    }
                })
            }
        </g>
    }
}

export class RMICompass extends Component {
    constructor(props) {
        super(props)
        this.width = 600
        this.height = 600
        this.top = -300
        this.left = -300
    }

    render() {
        const mainTicks = Array.from(Array(72)).map((_, i) => i * 5).filter(v => v % 30 === 0)
        const majorTicks = Array.from(Array(72)).map((_, i) => i * 5).filter(v => v % 30 !== 0 && v % 10 === 0)
        const minorTicks = Array.from(Array(72)).map((_, i) => i * 5).filter(v => v % 30 !== 0 && v % 10 !== 0)

        return <g id="RMICompass" viewBox={`${this.left} ${this.top} ${this.width} ${this.height}`}>
            {/* <circle x={0} y={0} r={370} fillOpacity={1.0} fill="red"></circle> */}
            <circle x={0} y={0} r={300} fillOpacity={1}></circle>
            {
                mainTicks.map(i => <rect x={0} y={0} width={8} height={50} transform={`translate(-4,-300) rotate(${i},4,300)`} fill="white" stroke="white"></rect>)
            }
            {
                majorTicks.map(i => <rect x={0} y={0} width={5} height={40} transform={`translate(-2.5,-300) rotate(${i},2.5,300)`} fill="white" stroke="white"></rect>)
            }
            {
                minorTicks.map(i => <rect x={0} y={0} width={5} height={20} transform={`translate(-2.5,-300) rotate(${i},2.5,300)`} fill="white" stroke="white"></rect>)
            }
            {
                mainTicks.map(i => <text transform={`translate(0,-210) rotate(${i},0,210)`} dominantBaseline={"middle"} textAnchor="middle" stroke="white" fill="white" x={0} y={0} fontSize={80} fontFamily="lenya69">{`${i === 0 ? "С" : i / 10}`}</text>)
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
        this.edge = 77
    }
    render() {
        const mainTicks = Array.from(Array(72)).map((_, i) => i * 5).filter(v => v % 30 === 0)
        const labels_upper = [6, 30]
        const labels_lower = [12, 24]
        return <g id="RMIFace" viewBox={`${this.left} ${this.top} ${this.width} ${this.height}`}>
            <circle x={0} y={0} r={370} fillOpacity={1}></circle>
            {
                mainTicks.map(i => <rect x={0} y={0} width={5} height={60} transform={`translate(-2.5,-345) rotate(${i},2.5,345)`} fill="orange" stroke="orange"></rect>)
            }
            <g transform="rotate(0,0,0)">
                <RMICompass></RMICompass>
            </g>
            <path transform="translate(0,-300)" fill="white" d={`M 0 0 L ${this.edge / 2} ${-this.edge / 2 * Math.sqrt(3)} L ${-this.edge / 2} ${-this.edge / 2 * Math.sqrt(3)} Z`}></path>
            {
                labels_upper.map(l => <text fontWeight={"bold"} transform={`translate(${Math.sin(l * 10 / 180 * Math.PI) * 315},${-Math.cos(l * 10 / 180 * Math.PI) * 315 - 30})`} dominantBaseline={"middle"} textAnchor="middle" stroke="orange" fill="orange" x={0} y={0} fontSize={50} fontFamily="lenya69">{l}</text>)
            }
            {
                labels_lower.map(l => <text fontWeight={"bold"} transform={`translate(${Math.sin(l * 10 / 180 * Math.PI) * 345},${-Math.cos(l * 10 / 180 * Math.PI) * 345 - 30})`} dominantBaseline={"middle"} textAnchor="middle" stroke="orange" fill="orange" x={0} y={0} fontSize={50} fontFamily="lenya69">{l}</text>)
            }
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
            <rect x={-this.width / 2} y={-this.height / 2 - 100} width={this.width} height={this.height} fill="rgb(101,139,148)" fillOpacity={1}></rect>
            <text stroke="white" fill="white" x={-210} y={410} fontSize={70} letterSpacing={-3} textLength={130} lengthAdjust="spacingAndGlyphs" fontWeight={"bold"} fontFamily="lenya69">APK</text>
            <text stroke="white" fill="white" x={210 - 130} y={410} fontSize={70} letterSpacing={-3} textLength={130} lengthAdjust="spacingAndGlyphs" fontWeight={"bold"} fontFamily="lenya69">APK</text>
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

export class AGRBall extends Component {
    constructor(props) {
        super(props)
        this.width = 4 * props.radius
        this.height = 2 * props.radius
        this.left = -2 * props.radius
        this.top = - props.radius

        this.ticks = [-45, -40, -35, -30, -25, -20, -15, -10, -5, 5, 10, 15, 20, 25, 30, 35, 40, 45]
        this.widths = [6, 36, 6, 36, 6, 36, 6, 12, 3, 3, 12, 6, 36, 6, 36, 6, 36, 6]

        this.hideTick = [10, 20, 30, -10, -20, -30]
        this.hideWidth = [6, 6, 6, 6, 6, 6]
        this.hideFont = [40, 50, 60, 40, 50, 60]



    }

    render() {

        const r = this.props.radius
        return <g id="AGRBall" viewBox={`${this.left} ${this.top} ${this.width} ${this.height}`}>
            <rect x={this.left} y={this.top} width={this.width} height={this.height / 2} fill="rgb(187,231,244)"></rect>
            <rect x={this.left} y={0} width={this.width} height={this.height / 2} fill="rgb(117,64,58)"></rect>

            {
                this.ticks.map((t, i) => (
                    <line x1={-r * this.widths[i] / 90.0 - r} x2={r * this.widths[i] / 90.0 - r} y1={this.height / 180.0 * t} y2={this.height / 180.0 * t} strokeWidth={2} stroke={t < 0 ? "black" : "white"}></line>
                ))
            }
            {
                this.hideTick.map((t, i) => (
                    <line x1={-r * this.hideWidth[i] / 90.0 - r} x2={r * this.hideWidth[i] / 90.0 - r} y1={this.height / 180.0 * t} y2={this.height / 180.0 * t} strokeWidth={10} stroke={t < 0 ? "rgb(187,231,244)" : "rgb(117,64,58)"}></line>
                ))
            }
            {
                this.hideTick.map((t, i) => (
                    <text fontWeight={"bold"} dominantBaseline={"middle"} textAnchor="middle" stroke={t > 0 ? "white" : "black"} fill={t > 0 ? "white" : "black"} x={-r} y={this.height / 180.0 * t} fontSize={this.hideFont[i]} fontFamily="lenya69">{Math.abs(t)}</text>
                ))
            }
            <line x1={this.left} x2={-this.left} y1={0} y2={0} strokeWidth={2} stroke="white"></line>
            <line x1={-this.props.radius} x2={-this.props.radius} y1={this.top} y2={-this.top} strokeWidth={2} stroke="white"></line>
        </g >
    }
}

export class AGRShield extends Component {
    constructor(props) {
        super(props)
        this.width = 900
        this.height = 900
        this.left = -450
        this.top = -450
        this.mainTicks = [0, 90, 120, 240, 270]
        this.minorTicks = [130, 140, 160, 170, 190, 200, 220, 230]
        this.majorTicks = [150, 210]
        this.texts = [152, 208]
        this.ballRadius = 450
        this.edge = 50
    }

    render() {
        return <g id="AGRShield" viewBox={`${this.left} ${this.top} ${this.width} ${this.height}`}>
            {/* <circle x={0} y={0} r={500} fillOpacity={0.0}></circle> */}
            <g transform="translate(450,0)">
                <AGRBall radius={this.ballRadius}></AGRBall>
            </g>

            <circle x={0} y={0} r={380} stroke="rgb(20,10,10)" strokeWidth={140} strokeOpacity={1} fillOpacity={0}></circle>
            {
                this.mainTicks.map(i => <rect x={0} y={0} width={8} height={40} transform={`translate(-4,-350) rotate(${i},4,350)`} fill="white" stroke="white"></rect>)
            }
            {
                this.minorTicks.map(i => <rect x={0} y={0} width={5} height={20} transform={`translate(-2.5,-330) rotate(${i},2.5,330)`} fill="white" stroke="white"></rect>)
            }
            {
                this.majorTicks.map(i => <rect x={0} y={0} width={8} height={20} transform={`translate(-4,-330) rotate(${i},4,330)`} fill="white" stroke="white"></rect>)
            }
            {
                this.texts.map(i => <text fontWeight={"bold"} transform={`translate(${Math.sin(i / 180 * Math.PI) * 365},${-Math.cos(i / 180 * Math.PI) * 365})`} dominantBaseline={"middle"} textAnchor="middle" stroke="white" fill="white" x={0} y={0} fontSize={60} fontFamily="lenya69">{30}</text>)
            }
            <path transform="translate(0,310)" fill="white" d={`M 0 0 L ${this.edge / 2} ${this.edge / 2 * Math.sqrt(3)} L ${-this.edge / 2} ${this.edge / 2 * Math.sqrt(3)} Z`}></path>
            {/* <circle x={0} y={0} r={310} fillOpacity={0.5}></circle> */}
        </g >
    }


}

export class AGR extends Component {
    constructor(props) {
        super(props)
    }

    render() {
        return <g>
            <AGRShield></AGRShield>
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
            <g transform="translate(1487,750)">
                <AGR></AGR>
            </g>
        </g>
    }
}