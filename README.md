# PyPix

> Python utility for generating QR Codes for Brazilian Pix payments.

**Python · Pix · QR Code · EMV payloads · Tkinter**

| | |
|---|---|
| **Type** | Python library / utility |
| **Domain** | Payments / Brazilian Pix |
| **Focus** | Pix QR Code generation |
| **Status** | Public technical project |

## Overview

PyPix provides a simple Python interface for generating Pix payment QR Codes from payment information such as Pix key, amount, merchant name, city and optional description.

The project also includes a lightweight desktop interface for interactive QR Code generation.

## Capabilities

- Generate Pix payment QR Codes.
- Accept Pix key, amount and merchant information.
- Include an optional transaction description.
- Save generated QR Codes as image files.
- Use the generator programmatically from Python.
- Run a simple Tkinter graphical interface.

## Programmatic usage

```python
from pypix_qrcode import generate_pix_qrcode, save_pix_qrcode

pix_key = "your-pix-key"
amount = 100.00
merchant_name = "Merchant Name"
city = "SAO PAULO"
description = "Example payment"

qr_image = generate_pix_qrcode(
    pix_key,
    amount,
    merchant_name,
    city,
    description,
)

save_pix_qrcode(qr_image, "pix-qrcode.png")
```

## Graphical interface

```python
from pypix_qrcode import run_gui

run_gui()
```

## Installation

Clone the repository and install its dependencies according to the project configuration.

If using a packaged release compatible with this source:

```bash
pip install pix_qrcode
```

## Architecture

```text
Payment Data
    │
    ▼
Pix Payload Builder
    │
    ▼
QR Code Generator
    │
 ┌──┴───────────┐
 │              │
Python API   Tkinter UI
```

## Security and payment note

This project generates payment payloads/QR Codes. It does **not** replace payment-provider confirmation or bank-side transaction validation.

Applications integrating Pix should independently validate payment status through the appropriate financial institution or payment provider before considering a transaction settled.

## Why this project is public

PyPix is part of my public engineering portfolio and represents work around Brazilian payment technology and reusable Python tooling.

## License

MIT.

---

**Jean Pires** · [GitHub](https://github.com/jdrpires) · [Portfolio](https://github.com/jdrpires/jdrpires)
