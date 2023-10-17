import Names

@main
struct App {
    static func main() {
        for name in Names.getNames() {
           print("hello \(name)")
        }
        GeneratedCode().main()
    }
}
