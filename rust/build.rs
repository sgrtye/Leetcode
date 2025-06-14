use std::fs::{self, File};
use std::io::Write;
use std::path::Path;

fn main() {
    let leetcode_dir = "src/leetcode";
    let mod_file_path = Path::new(leetcode_dir).join("mod.rs");

    let entries = fs::read_dir(leetcode_dir)
        .expect("Failed to read the leetcode directory")
        .filter_map(Result::ok)
        .filter(|entry| entry.path().extension().map(|e| e == "rs").unwrap_or(false))
        .collect::<Vec<_>>();

    let mut mod_file = File::create(mod_file_path).expect("Failed to create mod.rs");

    // Don't create a global Solution struct
    for entry in entries {
        let file_name = entry.file_name().into_string().unwrap();
        if file_name != "mod.rs" {
            let module_name = file_name.trim_end_matches(".rs");
            writeln!(mod_file, "pub mod {} {{", module_name).expect("Failed to write module start");
            writeln!(mod_file, "    pub struct Solution;").expect("Failed to write local Solution struct");
            writeln!(mod_file, "    include!(\"{}\");", file_name).expect("Failed to write include");
            writeln!(mod_file, "}}").expect("Failed to write module end");
            writeln!(mod_file).expect("Failed to write newline");
        }
    }

    println!("cargo:rerun-if-changed={}", leetcode_dir);
}