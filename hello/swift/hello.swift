import People

@main
struct App {
    static func main() {
        for name in People.getNames() {
           print("hello \(name)")
        }
        GeneratedCode().main()
    }
}
