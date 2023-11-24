/// <reference types="@microsoft/msfs-types/Pages/VCockpit/Core/VCockpit" />

import { FSComponent } from "@microsoft/msfs-sdk";
import { MyComponent } from "./MyComponent";

class MyInstrument extends BaseInstrument {
  get templateID(): string {
    return "MyInstrument";
  }

  public connectedCallback(): void {
    super.connectedCallback();

    FSComponent.render(
      <MyComponent />,
      document.getElementById("InstrumentContent")
    );
  }
}

registerInstrument("my-instrument", MyInstrument);
