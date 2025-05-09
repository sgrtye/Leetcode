use std::fs::{self, File};
use std::io::Write;
use std::path::Path;

fn main() {
    let leetcode_dir = "src/leetcode";
    let mod_file_path = Path::new(leetcode_dir).join("mod.rs");

    // Get all the `.rs` files in the leetcode folder
    let entries = fs::read_dir(leetcode_dir)
        .expect("Failed to read the leetcode directory")
        .filter_map(Result::ok)
        .filter(|entry| entry.path().extension().map(|e| e == "rs").unwrap_or(false))
        .collect::<Vec<_>>();

    // Start writing the mod.rs file
    let mut mod_file = File::create(mod_file_path).expect("Failed to create mod.rs");

    // Write `pub mod <filename>` for each `.rs` file
    for entry in entries {
        let file_name = entry.file_name().into_string().unwrap();
        if file_name != "mod.rs" {
            let module_name = file_name.trim_end_matches(".rs");
            writeln!(mod_file, "pub mod {};", module_name).expect("Failed to write to mod.rs");
        }
    }

    println!("cargo:rerun-if-changed={}", leetcode_dir); // Tell Cargo to rerun build.rs if the directory changes
}
