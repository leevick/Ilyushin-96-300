import { Component } from "react";
import pu56 from "./pu56.png"
import pu56_full from "./pu56.jpg"


export default class PU56 extends Component {
    constructor(props) {
        super(props)
        this.width = 4700
        this.height = 800
        this.left = 0
        this.top = 0
    }

    render() {
        const r = 175
        const ca = 60
        const dr = 15

        var str = `M ${-r * Math.sin(Math.PI / 180 * ca)} ${-r * Math.cos(Math.PI / 180 * ca)} `

        for (var i = 1; i < 2 * ca - 4; i = i + 1) {
            str += `L ${(r - (i * dr / (2 * ca))) * Math.sin(Math.PI / 180 * (-ca + i))} ${-(r - (i * dr / (2 * ca))) * Math.cos(Math.PI / 180 * (-ca + i))} `
        }

        str += `A ${dr} ${dr} 0 0 0 ${(r + ((2 * ca - 5) * dr / (2 * ca))) * Math.sin(Math.PI / 180 * (-ca + (2 * ca - 5)))} ${-(r + ((2 * ca - 5) * dr / (2 * ca))) * Math.cos(Math.PI / 180 * (-ca + (2 * ca - 5)))} `

        for (var i = 2 * ca - 5; i >= 1; i = i - 1) {
            str += `L ${(r + (i * dr / (2 * ca))) * Math.sin(Math.PI / 180 * (-ca + i))} ${-(r + (i * dr / (2 * ca))) * Math.cos(Math.PI / 180 * (-ca + i))} `
        }


        return <g id="PU56" viewBox={`${this.left} ${this.top} ${this.width} ${this.height}`}>
            {/* <image x={0} y={0} width={4700} height={800} href={pu56_full} />
            <image x={316} y={0} width={4384} height={800} href={pu56} /> */}
            <rect x={0} y={0} width={this.width} height={this.height} fill="rgb(101,139,148)" fillOpacity={0}></rect>
            <g transform="translate(100,0)">
                <text x={850} y={75} letterSpacing={-3} textLength={110} fontSize={60} lengthAdjust="spacingAndGlyphs" dominantBaseline="central" stroke="white" fill="white" fontFamily="lenya69">V/M</text>
                <text x={385} y={300} letterSpacing={-3} textLength={110} fontSize={60} lengthAdjust="spacingAndGlyphs" dominantBaseline="central" stroke="white" fill="white" fontFamily="lenya69">V/M</text>
                <text x={1600} y={75} textLength={30} fontSize={60} lengthAdjust="spacingAndGlyphs" dominantBaseline="central" stroke="white" fill="white" fontFamily="lenya69">H</text>
                <text x={1630} y={85} textLength={60} fontSize={30} lengthAdjust="spacingAndGlyphs" dominantBaseline="central" stroke="white" fill="white" fontFamily="lenya69">ЭШ</text>
                <text x={2070} y={75} textLength={150} fontSize={60} lengthAdjust="spacingAndGlyphs" dominantBaseline="central" stroke="white" fill="white" fontFamily="lenya69">ВНИЗ</text>
                <g transform="translate(2250,295)">
                    <path fill="white" stroke="white" strokeWidth={1} d="M 2.5 0 l 0 -80 l 5 0 l -7.5 -30 l -7.5 30 l 5 0 l 0 80"></path>
                    <g transform="rotate(180),translate(0,-200)">
                        <path fill="white" stroke="white" strokeWidth={1} d="M 2.5 0 l 0 -80 l 5 0 l -7.5 -30 l -7.5 30 l 5 0 l 0 80"></path>
                    </g>
                </g>
                <path d="M 2300 450 l 50 0 l 120 200" stroke="white" fill="none" strokeWidth={5}></path>
                <text x={2465} y={75} textLength={100} fontSize={60} lengthAdjust="spacingAndGlyphs" dominantBaseline="central" stroke="white" fill="white" fontFamily="lenya69">±Vy</text>
                <text x={2570} y={75} textLength={30} fontSize={60} lengthAdjust="spacingAndGlyphs" dominantBaseline="central" stroke="white" fill="white" fontFamily="lenya69">/</text>
                <text x={2620} y={75} textLength={120} fontSize={60} lengthAdjust="spacingAndGlyphs" dominantBaseline="central" stroke="white" fill="white" fontFamily="lenya69">УНТ</text>
                <text x={2055} y={800 - 90} textLength={180} fontSize={60} lengthAdjust="spacingAndGlyphs" dominantBaseline="central" stroke="white" fill="white" fontFamily="lenya69">ВВЕРХ</text>
                <text x={3660} y={75} textLength={220} fontSize={60} lengthAdjust="spacingAndGlyphs" dominantBaseline="central" stroke="white" fill="white" fontFamily="lenya69">ЗПУ/ЗК</text>
                <text x={4250} y={75} textLength={220} fontSize={60} lengthAdjust="spacingAndGlyphs" dominantBaseline="central" stroke="white" fill="white" fontFamily="lenya69">ПУ-56М</text>
                <text x={3000} y={75} textLength={250} fontSize={60} lengthAdjust="spacingAndGlyphs" dominantBaseline="central" stroke="white" fill="white" fontFamily="lenya69">ОБР ЛУЧ</text>
                <text x={4440} y={470} letterSpacing={-3} textLength={120} fontSize={60} lengthAdjust="spacingAndGlyphs" dominantBaseline="central" stroke="white" fill="white" fontFamily="lenya69">ДИР</text>
                <g transform="translate(3785,640)">
                    {/* <circle r={140}></circle> */}
                    <path d="M -330 20 l 135 0 l 50 -20" stroke="white" strokeWidth={5} fill="none"></path>
                    <text x={-315} y={-30} textLength={110} fontSize={60} lengthAdjust="spacingAndGlyphs" dominantBaseline="central" stroke="white" fill="white" fontFamily="lenya69">АВТ</text>
                    <path d="M -330 20 l 135 0 l 50 -20" stroke="white" strokeWidth={5} fill="none"></path>
                    {
                        [0, 5, 10, 15, 20, 25, 30].map((v, i) => <line stroke="white" strokeWidth={5} x1={160 * Math.cos(Math.PI / 6 * i - Math.PI / 12)} x2={180 * Math.cos(Math.PI / 6 * i - Math.PI / 12)} y1={-160 * Math.sin(Math.PI / 6 * i - Math.PI / 12)} y2={-180 * Math.sin(Math.PI / 6 * i - Math.PI / 12)} ></line>)
                    }
                    <g transform="rotate(15)">
                        <path d="M -160 0 a 160 160 0 0 1 320 0" stroke="white" strokeWidth={5} fill="none"></path>
                    </g>
                    <text x={-180} y={-135} textLength={30} fontSize={60} lengthAdjust="spacingAndGlyphs" dominantBaseline="central" stroke="white" fill="white" fontFamily="lenya69">5</text>
                    <text x={60} y={-190} textLength={50} fontSize={60} lengthAdjust="spacingAndGlyphs" dominantBaseline="central" stroke="white" fill="white" fontFamily="lenya69">15</text>
                    <text x={175} y={75} textLength={60} fontSize={60} lengthAdjust="spacingAndGlyphs" dominantBaseline="central" stroke="white" fill="white" fontFamily="lenya69">30</text>
                </g>

                <g transform="translate(765,640)">
                    {/* <circle r={110} fillOpacity={0.2}></circle> */}
                </g>

                <g transform="translate(3040,130)">
                    {/*
                    <rect rx={10} x={0} y={0} width={180} height={180}></rect>
                    <rect rx={10} x={0} y={200} width={180} height={180}></rect>
                    <rect rx={10} x={0} y={400} width={180} height={180}></rect>
                    <rect rx={10} x={200} y={200} width={180} height={180}></rect>
                    <rect rx={10} x={200} y={400} width={180} height={180}></rect>
                    */}
                    <g width={180} height={180} transform="translate(0,0)">


                    </g>
                    <g transform="translate(0,200)">
                        <g id="PU56KZONA" viewBox="0 0 180 180">
                            <text x={10} y={45} textLength={160} fontSize={60} lengthAdjust="spacingAndGlyphs" dominantBaseline="central" stroke="white" fill="white" fontFamily="lenya69">КЗОНА</text>
                        </g>
                    </g>

                    <g transform="translate(0,400)">
                        <g id="PU56POS" viewBox="0 0 180 180">
                            <text x={40} y={45} textLength={100} fontSize={60} lengthAdjust="spacingAndGlyphs" dominantBaseline="central" stroke="white" fill="white" fontFamily="lenya69">ПОС</text>
                        </g>
                    </g>

                    <g transform="translate(200,200)">
                        <g id="PU56GNAV" viewBox="0 0 180 180" >
                            <text x={30} y={45} textLength={120} fontSize={60} lengthAdjust="spacingAndGlyphs" dominantBaseline="central" stroke="white" fill="white" fontFamily="lenya69">ГНАВ</text>
                        </g>
                    </g>
                    <g transform="translate(200,400)">
                        <g id="PU56ZPU" viewBox="0 0 180 180">
                            <text x={40} y={45} textLength={100} fontSize={60} lengthAdjust="spacingAndGlyphs" dominantBaseline="central" stroke="white" fill="white" fontFamily="lenya69">ЗПУ</text>
                        </g>
                    </g>
                </g>

                <g transform="translate(1600,130)">
                    {/* 
                    <rect rx={10} x={0} y={400} width={180} height={180}></rect>
                    <rect rx={10} x={200} y={400} width={180} height={180}></rect>
                     */}

                    <g transform="translate(200,400)">
                        <g id="PU56VNAV" viewBox="0 0 180 180">
                            <text x={30} y={45} textLength={120} fontSize={60} lengthAdjust="spacingAndGlyphs" dominantBaseline="central" stroke="white" fill="white" fontFamily="lenya69">ВНАВ</text>
                        </g>
                    </g>
                    <g transform="translate(0,400)">
                        <g id="PU56VEIS" viewBox="0 0 180 180">
                            <text x={45} y={45} textLength={90} fontSize={60} lengthAdjust="spacingAndGlyphs" dominantBaseline="central" stroke="white" fill="white" fontFamily="lenya69">ВЫС</text>
                        </g>
                    </g>

                </g>
                <g transform="translate(990,130)">
                    <g transform="translate(0,400)">
                        <g id="PU56ESHEL" viewBox="0 0 180 180">
                            <text x={30} y={45} textLength={120} fontSize={60} lengthAdjust="spacingAndGlyphs" dominantBaseline="central" stroke="white" fill="white" fontFamily="lenya69">ЭШЕЛ</text>
                        </g>
                    </g>
                    {/* <rect rx={10} x={0} y={400} width={180} height={180}></rect> */}
                </g>
                <g transform="translate(2500,130)">
                    {/* <rect rx={10} x={0} y={400} width={180} height={180}></rect> */}
                    <g transform="translate(0,400)">
                        <g id="PU56VSKOR" viewBox="0 0 180 180">
                            <text x={15} y={45} textLength={150} fontSize={60} lengthAdjust="spacingAndGlyphs" dominantBaseline="central" stroke="white" fill="white" fontFamily="lenya69">ВСКОР</text>
                        </g>
                    </g>
                </g>
                <g transform="translate(4200,130)">
                    {/* <rect rx={10} x={0} y={200} width={180} height={180}></rect>
                    <rect rx={10} x={0} y={400} width={180} height={180}></rect> */}

                    <g transform="translate(0,200)">
                        <g id="PU56AP" viewBox="0 0 180 180">
                            <text x={60} y={45} textLength={60} fontSize={60} lengthAdjust="spacingAndGlyphs" dominantBaseline="central" stroke="white" fill="white" fontFamily="lenya69">АП</text>
                        </g>
                    </g>
                    <g transform="translate(0,400)">
                        <g id="PU56OTKLAP" viewBox="0 0 180 180">
                            <text x={30} y={60} textLength={120} fontSize={60} lengthAdjust="spacingAndGlyphs" dominantBaseline="central" stroke="white" fill="white" fontFamily="lenya69">ОТКЛ</text>
                            <text x={60} y={120} textLength={60} fontSize={60} lengthAdjust="spacingAndGlyphs" dominantBaseline="central" stroke="white" fill="white" fontFamily="lenya69">АП</text>
                        </g>
                    </g>
                </g>
                <g transform="translate(150,130)">
                    {/*
                    <rect rx={10} x={0} y={0} width={180} height={180}></rect>
                    <rect rx={10} x={0} y={200} width={180} height={180}></rect>
                    <rect rx={10} x={0} y={400} width={180} height={180}></rect>
                    <rect rx={10} x={200} y={400} width={180} height={180}></rect> 
                    */}

                    <g transform="translate(0,0)">
                        <g id="PU56AT" viewBox="0 0 180 180">
                            <text x={60} y={45} textLength={60} fontSize={60} lengthAdjust="spacingAndGlyphs" dominantBaseline="central" stroke="white" fill="white" fontFamily="lenya69">АТ</text>
                        </g>
                    </g>
                    <g transform="translate(0,200)">
                        <g id="PU56STAB" viewBox="0 0 180 180">
                            <text x={30} y={45} textLength={120} fontSize={60} lengthAdjust="spacingAndGlyphs" dominantBaseline="central" stroke="white" fill="white" fontFamily="lenya69">СТАБ</text>
                        </g>
                    </g>
                    <g transform="translate(0,400)">
                        <g id="PU56OTKLAT" viewBox="0 0 180 180">
                            <text x={30} y={60} textLength={120} fontSize={60} lengthAdjust="spacingAndGlyphs" dominantBaseline="central" stroke="white" fill="white" fontFamily="lenya69">ОТКЛ</text>
                            <text x={60} y={120} textLength={60} fontSize={60} lengthAdjust="spacingAndGlyphs" dominantBaseline="central" stroke="white" fill="white" fontFamily="lenya69">АТ</text>
                        </g>
                    </g>
                    <g transform="translate(200,400)">
                        <g id="PU56SKOR" viewBox="0 0 180 180">
                            <text x={30} y={45} textLength={120} fontSize={60} lengthAdjust="spacingAndGlyphs" dominantBaseline="central" stroke="white" fill="white" fontFamily="lenya69">СКОР</text>
                        </g>
                    </g>
                </g>

            </g>
            {/* <g transform="translate(720,170)">
                <rect ry={20} x={0} y={0} width={565} height={200} rx={20}></rect>
                <rect ry={20} x={740} y={0} width={565} height={200} rx={20}></rect>
                <rect ry={20} x={1700} y={0} width={565} height={200} rx={20}></rect>
                <rect ry={20} x={2870} y={0} width={565} height={200} rx={20}></rect>
            </g> 
            {/* <rect fillOpacity={1} x={2210} y={150} width={80} height={500}></rect> */}
            <text x={40} y={470} letterSpacing={-3} textLength={120} fontSize={60} lengthAdjust="spacingAndGlyphs" dominantBaseline="central" stroke="white" fill="white" fontFamily="lenya69">ДИР</text>
            <text x={40} y={160} letterSpacing={-3} textLength={120} fontSize={60} lengthAdjust="spacingAndGlyphs" dominantBaseline="central" stroke="white" fill="white" fontFamily="lenya69">ЯРК</text>
            {/* <circle cx={100} cy={300} r={80}></circle> */}
            <g transform="translate(1500,640)">
                <path d="M -210 30 l 100 -40" stroke="white" strokeWidth={5} fill="none"></path>
                <path fill="white" stroke="white" strokeWidth={1} d={str}></path>
                {/* <circle fillOpacity={1} r={120}></circle> */}
            </g>
            <g transform="translate(870,640)">
                <path d="M -210 30 l 100 -40" stroke="white" strokeWidth={5} fill="none"></path>
                <path fill="white" stroke="white" strokeWidth={1} d={str}></path>
                {/* <circle fillOpacity={1} r={120}></circle> */}
            </g>
            {/*
            <g transform="translate(4600,560)">
                <path d="M -35 0 a 35 35 0 0 1 70 0 l 0 70 a 35 35 0 0 1 -70 0"></path>
            </g>
            <g transform="translate(100,560)">
                <path d="M -35 0 a 35 35 0 0 1 70 0 l 0 70 a 35 35 0 0 1 -70 0"></path>
            </g>
            */}
        </g>
    }
}