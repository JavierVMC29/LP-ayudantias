import 'dart:convert';
import 'dart:io';

void main() {
  // Read some data.
  final fileData = _readFileSync();
  final jsonData = jsonDecode(fileData);

  // Use that data.
  print('Number of JSON keys: ${jsonData.length}');
  print(jsonData);
  print(jsonData.map((t) => t['name']));
}

final path = 'example.json';

String _readFileSync() {
  final file = File(path);
  final contents = file.readAsStringSync();
  return contents.trim();
}
