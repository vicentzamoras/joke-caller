# Joke Caller

A chat model that calls someone by name and tells them a joke.

> A test plugin for [dashAI](https://github.com/DashAISoftware/DashAI), installed by its repo link or a local `.zip`. It is not in the plugin store.

## Components

| Class | Type |
| --- | --- |
| `JokeCallerTask` | GenerativeTask |
| `JokeCallerModel` | GenerativeModel |

## Usage

In the plugin's settings, set the **Name** and the **Language**. Then, in **Generative**, choose the **Joke caller (plugin)** task and model, and write anything:

| Name | Language | Reply |
| --- | --- | --- |
| Juan | Spanish | `Oye, Juan: "<a joke in Spanish>"` |
| Antonio | English | `Hey, Antonio: "<a joke in English>"` |

## Details

- **Requires:** dashAI 0.10.0 or newer, and the [Shout Chat](https://github.com/vicentzamoras/shout-chat) plugin 1.0.0 or newer.
- **Dependencies:** `pyjokes>=0.6`.
- **Releases:** Releases are built and signed by this repo's GitHub Actions workflow (`.github/workflows/release.yaml`): dashAI shows them as verified.

## License

MIT
