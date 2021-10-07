# EndoLink Angular App
This project was generated with [Angular CLI](https://github.com/angular/angular-cli) version 12.2.8.

## Project Structure
All components are to be declared in `/src/app/components`. The individual components may include sub-components which are unique to their parent. A parent-component may also implement a separate `shared.scss` next to their `.component.scss` for styling that is shared with child-components.

## Development server
You can either run `docker compose up` in the root of the project or `ng serve` for a dev server. Depending on your choice the frontend will be accessible either through `http://localhost:8080` or `http://localhost:4200/`. The app will automatically reload if you change any of the source files.

## Build
Run `ng build` to build the project. The build artifacts will be stored in the `dist/` directory.

## Running unit tests
Run `ng test` to execute the unit tests via [Karma](https://karma-runner.github.io).
