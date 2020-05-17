extern crate amethyst;
use amethyst::prelude::*;
extern crate rand;
extern crate glob;
extern crate chrono; 
use self::glob::glob;
use rand::seq::SliceRandom;
use chrono::{Timelike, Utc};
use std::time::Duration;
use log::info;
use std::path::Path;
use std::fs;
use serde::Deseralize;
struct BattleUi{
    mut player_pokemon : String;
    mut opponent_pokemon: String;
    player_pokemon_moves: vec![String];
    mut ui_background: String;
    mut song_played: String,
    fight_button: vec![String];
    is_ui_active: bool;
    pokemon_button: vec![String];
    item_button: vec![String];
    player_pokemon_hp: u8;
    mut player_name: String;
}
// Defines the localhost struct
pub struct LocalHost{
    Trainer1: struct BattleUi;
    Trainer2: struct BattleUi;
}

#[repr(C)]
pub struct TrainerData{
    mut Name: String;
    mut Image_url: String;
    mut Time_Spent: u32;
    mut Pokemon1: [];
    mut Pokemon2: [];
    mut Pokemon3: [];
    mut Pokemon4: [];
    mut Pokemon5: [];
    mut Pokemon6: [];
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
    image_battle = image_battle.replace("resources", "../resources");
    return image_battle;
}
// // Loads in a pokemon data for the battle
// fn read_pokemon_data(pokemon_name: String, back_sprite: String, icon: String, hp: u32, move1: String, move2: String, move3: String, move4: String, item: String){
    
//}
// Reads the json data 
// fn read_player_data(){
//     // Path assigned to the json files
//     let json_directory = "../../../launcher/trainer_data"

// }
// Does the battle background rendering
fn battle_engine_screen_render(time_of_day: String) -> String{
    // Put a bunch of strings together
    let path = "./resources/graphics/battle_backgrounds/".to_owned();
    let selector: &str = "*";
    let new_path = path + &time_of_day + selector;

    // Now grabs a random image using the criteria
    let time_of_day_image = rand_image(new_path.to_string(), "".to_string());
    return time_of_day_image;
}

fn load_sprite(world: &mut World, Sprite_location: String, Sprite_Sheet: String) -> Vec<SpriteRender> {
    // Load the texture for our sprites. We'll later need to
    // add a handle to this texture to our `SpriteRender`s, so
    // we need to keep a reference to it.
    let texture_handle = {
        let loader = world.read_resource::<Loader>();
        let texture_storage = world.read_resource::<AssetStorage<Texture>>();
        
        loader.load(
            Sprite_location,
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
            Sprite_Sheet,
            SpriteSheetFormat(texture_handle),
            (),
            &sheet_storage,
        )
    };

    // Create our sprite renders. Each will have a handle to the texture
    // that it renders from. The handle is safe to clone, since it just
    // references the asset.
    (0..1)
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

impl SimpleState for BattleUi{
    // Passes in the data from Python to here
     extern "C" fn parse_player_data(player1: struct TrainerData) -> struct BattleUi{
        println!("{:?}", trainer);
    }
    // Localhost function
    extern "C" fn parse_player_localhost(player1: struct TrainerData, player2: struct BattleUi) -> struct LocalHost{
        println!("{:?}", trainer);
    }
    fn on_start(&mut self, _data: StateData<'_, GameData<'_, '_>>) {
        let now = Utc::now();
        let (is_pm, hour) = now.hour12();
        let image = String::new();
        println!("{}", hour);
        // Morning
        if hour >= 7 && hour <= 11 && !is_pm{
            println!("current time is {} am", hour);
            image = battle_engine_screen_render("morning".to_string());
            println!("{:?} ", image);
        }
        // Afternoon trigger
        if hour <= 5 && is_pm || hour  == 12 && is_pm{
            println!("current time is {} pm", hour);
            image = battle_engine_screen_render("afternoon".to_string());
            println!("{:?} ", image);
        }
        
        // Night/evening
        if hour >= 6 && is_pm ||  hour >= 1 && !is_pm && hour <= 6 && !is_pm || hour >= 12 && !is_pm{
            println!("current time is {} ", hour);
            image = battle_engine_screen_render("night".to_string());
            println!("{:?} is the image, somewhere in the night time", image);
        }
        
        let mut battle_ui_player1 = BattleUi{};
        let mut battle_ui_player2 = BattleUi{};
        battle_ui_player1.ui_background = image;
    }
}

