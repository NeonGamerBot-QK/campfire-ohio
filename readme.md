<a id="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">

<h3 align="center">Water Space Platformer</h3>

  <p align="center">
    A 2D underwater platformer where you swim through the deep, battle aquatic mobs, and level up — built at Hack Club Campfire Ohio.
    <br />
    <a href="https://github.com/NeonGamerBot-QK/campfire-ohio"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/NeonGamerBot-QK/campfire-ohio/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    &middot;
    <a href="https://github.com/NeonGamerBot-QK/campfire-ohio/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

A 2D underwater platformer built with Pygame at Hack Club Campfire Ohio. Swim around, shoot sea pickles at hostile fish, and level up.

- **Movement**: WASD/Arrow keys to swim in any direction
- **Combat**: Spacebar to shoot projectiles at enemies
- **NPCs**: Six enemy variants that patrol, chase, and shoot back
- **Progression**: XP on kills, leveling increases attack damage and max HP
- **Game over**: Press R to restart

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python-shield]][Python-url]
* [![Pygame][Pygame-shield]][Pygame-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running, follow these steps.

### Prerequisites

- Python 3.10 or later

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/NeonGamerBot-QK/campfire-ohio.git
   cd campfire-ohio
   ```
2. Create and activate a virtual environment
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies
   ```sh
   pip install pygame pygame-menu
   ```
4. Run the game
   ```sh
   python main.py
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE -->
## Usage

| Key | Action |
|---|---|
| `W` / `↑` | Swim up |
| `A` / `←` | Swim left |
| `S` / `↓` | Swim down |
| `D` / `→` | Swim right |
| `Space` | Attack (shoot projectile) |
| `R` | Restart after game over |

Defeat NPCs to earn XP. Each level-up increases your attack damage and max HP.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Underwater stage with swimming and combat
- [ ] Space stage with helmet and oxygen mechanics
- [ ] Stage transition system (water ↔ space)
- [ ] Space boss encounter
- [ ] Water boss encounter

See the [open issues](https://github.com/NeonGamerBot-QK/campfire-ohio/issues) for a full list of proposed features and known issues.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'feat: add some amazing feature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Top Contributors

<a href="https://github.com/NeonGamerBot-QK/campfire-ohio/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=NeonGamerBot-QK/campfire-ohio" alt="contrib.rocks image" />
</a>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Hack Club](https://hackclub.com) — for hosting Campfire Ohio
* [Pygame](https://www.pygame.org/) — game engine
* [pygame-menu](https://pygame-menu.readthedocs.io/) — menu system

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/NeonGamerBot-QK/campfire-ohio.svg?style=for-the-badge
[contributors-url]: https://github.com/NeonGamerBot-QK/campfire-ohio/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/NeonGamerBot-QK/campfire-ohio.svg?style=for-the-badge
[forks-url]: https://github.com/NeonGamerBot-QK/campfire-ohio/network/members
[stars-shield]: https://img.shields.io/github/stars/NeonGamerBot-QK/campfire-ohio.svg?style=for-the-badge
[stars-url]: https://github.com/NeonGamerBot-QK/campfire-ohio/stargazers
[issues-shield]: https://img.shields.io/github/issues/NeonGamerBot-QK/campfire-ohio.svg?style=for-the-badge
[issues-url]: https://github.com/NeonGamerBot-QK/campfire-ohio/issues
[Python-shield]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[Pygame-shield]: https://img.shields.io/badge/Pygame-00CC00?style=for-the-badge&logo=python&logoColor=white
[Pygame-url]: https://www.pygame.org/
