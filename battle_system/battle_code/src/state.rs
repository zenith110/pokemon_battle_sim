use amethyst::{
    assets::{AssetStorage, Loader},
    core::transform::Transform,
    input::{get_key, is_close_requested, is_key_down, VirtualKeyCode},
    prelude::*,
    renderer::{Camera, ImageFormat, SpriteRender, SpriteSheet, SpriteSheetFormat, Texture},
    window::ScreenDimensions,
};
extern crate rand;
extern crate glob;
extern crate chrono; 
use self::glob::glob;
use rand::seq::SliceRandom;
use chrono::{Timelike, Utc};
use std::time::Duration;
use log::info;

pub struct MyState;

impl SimpleState for MyState {
    // On start will run when this state is initialized. For more
    // state lifecycle hooks, see:
    // https://book.amethyst.rs/stable/concepts/state.html#life-cycle
    fn on_start(&mut self, data: StateData<'_, GameData<'_, '_>>) {
        let world = data.world;

        // Get the screen dimensions so we can initialize the camera and
        // place our sprites correctly later. We'll clone this since we'll
        // pass the world mutably to the following functions.
        let dimensions = (*world.read_resource::<ScreenDimensions>()).clone();

        // Place the camera
        init_camera(world, &dimensions);

        // Load our sprites and display them
        let sprites = load_sprites(world);
        init_sprites(world, &sprites, &dimensions);
    }

    fn handle_event(
        &mut self,
        mut _data: StateData<'_, GameData<'_, '_>>,
        event: StateEvent,
    ) -> SimpleTrans {
        if let StateEvent::Window(event) = &event {
            // Check if the window should be closed
            if is_close_requested(&event) || is_key_down(&event, VirtualKeyCode::Escape) {
                return Trans::Quit;
            }

            // Listen to any key events
            if let Some(event) = get_key(&event) {
                info!("handling key event: {:?}", event);
            }

            // If you're looking for a more sophisticated event handling solution,
            // including key bindings and gamepad support, please have a look at
            // https://book.amethyst.rs/stable/pong-tutorial/pong-tutorial-03.html#capturing-user-input
        }

        // Keep going
        Trans::None
    }
}

fn init_camera(world: &mut World, dimensions: &ScreenDimensions) {
    // Center the camera in the middle of the screen, and let it cover
    // the entire screen
    let mut transform = Transform::default();
    transform.set_translation_xyz(dimensions.width() * 0.5, dimensions.height() * 0.5, 1.);

    world
        .create_entity()
        .with(Camera::standard_2d(dimensions.width(), dimensions.height()))
        .with(transform)
        .build();
}
// Lets us randomly select an image from the path provided
fn rand_image(image_path: String, mut image_battle: String)-> String{
    // Makes a list
    let mut vec_list = vec![];
    
    // Lets us grab the background signified from the image_path string
    for entry in glob(&image_path).expect("Failed to read glob pattern") {
                vec_list.push(entry.unwrap());
            }
    let rand_image = vec_list.choose(&mut rand::thread_rng());
    image_battle = rand_image.unwrap().to_str().unwrap().into();
    image_battle = image_battle.replace("\\", "/");
    return image_battle;
}

fn battle_engine_screen_render(time_of_day: String) -> String{
    // Put a bunch of strings together
    let path = "../resources/graphics/battle_backgrounds/".to_owned();
    let selector: &str = "*";
    let new_path = path + &time_of_day + selector;

    // Now grabs a random image using the criteria
    let time_of_day_image = rand_image(new_path.to_string(), "".to_string());
    let specific_image_file = time_of_day_image.replace("../resources/", "");
    return specific_image_file;
}
fn load_backgrounds_time(){
    let now = Utc::now();
    let (is_pm, hour) = now.hour12();
    println!("current time is {}", hour);
    // Morning
    if hour >= 7 && hour <= 12 && !is_pm{
        battle_engine_screen_render("morning".to_string());
    }
    // Afternoon trigger
    if hour <= 4 && hour  >= 12 && is_pm{
        battle_engine_screen_render("afternoon".to_string());
    }
    
    // Night/evening
    if hour >= 6 && is_pm ||  hour >= 1 && !is_pm && hour <= 6 && !is_pm{
        battle_engine_screen_render("night".to_string());
    }
}
fn load_sprites(world: &mut World) -> Vec<SpriteRender> {
    // Load the texture for our sprites. We'll later need to
    // add a handle to this texture to our `SpriteRender`s, so
    // we need to keep a reference to it.
    let texture_handle = {
        let loader = world.read_resource::<Loader>();
        let texture_storage = world.read_resource::<AssetStorage<Texture>>();
        let now = Utc::now();
        let (is_pm, hour) = now.hour12();
        let mut image = String::new();
        let image_dir = String::new();
        println!("current time is {}", hour);
        // Morning
        if hour >= 7 && hour <= 12 && !is_pm{
            image = battle_engine_screen_render("morning".to_string());
        }
        // Afternoon trigger
        if hour <= 4 && hour  >= 12 && is_pm{
            image = battle_engine_screen_render("afternoon".to_string());
        }
        
        // Night/evening
        if hour >= 6 && is_pm ||  hour >= 1 && !is_pm && hour <= 6 && !is_pm{
            image = battle_engine_screen_render("night".to_string());
        }
        
        loader.load(
            image,
            ImageFormat::default(),
            (),
            &texture_storage,
        )
    };

    // Load the spritesheet definition file, which contains metadata on our
    // spritesheet texture.
    let sheet_handle = {
        let loader = world.read_resource::<Loader>();
        let sheet_storage = world.read_resource::<AssetStorage<SpriteSheet>>();
        loader.load(
            "graphics/battle_backgrounds/battle_background.ron",
            SpriteSheetFormat(texture_handle),
            (),
            &sheet_storage,
        )
    };

    // Create our sprite renders. Each will have a handle to the texture
    // that it renders from. The handle is safe to clone, since it just
    // references the asset.
    (0..3)
        .map(|i| SpriteRender {
            sprite_sheet: sheet_handle.clone(),
            sprite_number: i,
        })
        .collect()
}

fn init_sprites(world: &mut World, sprites: &[SpriteRender], dimensions: &ScreenDimensions) {
    for (i, sprite) in sprites.iter().enumerate() {
        // Center our sprites around the center of the window
        let x = (i as f32 - 1.) * 100. + dimensions.width() * 0.5;
        let y = (i as f32 - 1.) * 100. + dimensions.height() * 0.5;
        let mut transform = Transform::default();
        transform.set_translation_xyz(x, y, 0.);

        // Create an entity for each sprite and attach the `SpriteRender` as
        // well as the transform. If you want to add behaviour to your sprites,
        // you'll want to add a custom `Component` that will identify them, and a
        // `System` that will iterate over them. See https://book.amethyst.rs/stable/concepts/system.html
        world
            .create_entity()
            .with(sprite.clone())
            .with(transform)
            .build();
    }
}
