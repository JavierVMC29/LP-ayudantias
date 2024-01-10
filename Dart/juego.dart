// Copyright (c) 2019, the Dart project authors.  Please see the AUTHORS file
// for details. All rights reserved. Use of this source code is governed by a
// BSD-style license that can be found in the LICENSE file.
import 'package:flutter/material.dart';
import 'dart:async';
import 'dart:math';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const MyHomePage(title: 'Mario Bross'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  final String title;
  const MyHomePage({
    Key? key,
    required this.title,
  }) : super(key: key);
  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  int health = 100;
  int score = 0;
  bool clockInitialized = false;
  static int clock = 10;
  static double mariox = 0.0;
  static double marioy = 1.0;
  static double javierx = 0.0;
  static double javiery = 1.0;
  double time = 0;
  double height = 0;
  double initialPos = javiery;
  String direction = "right";
  void preJump() {
    time = 0;
    initialPos = javiery;
  }

  void damage() {
    if ((javierx - mariox).abs() < 0.05 && (javiery - marioy).abs() < 0.05) {
      health -= 10;
    }
  }

  void clockTimer() {
    Timer.periodic(Duration(milliseconds: 1000), (timer) {
      if (clock > 0) {
        setState(() {
          clock -= 1;
        });
      } else {
        timer.cancel();
      }
    });
  }

  void jump() {
    score += 1;
    preJump();
    Timer.periodic(Duration(milliseconds: 50), (timer) {
      time += 0.05;
      height = -4.9 * time * time + 5 * time;
      if (initialPos - height > 1) {
        setState(() {
          javiery = 1;
        });
      } else {
        setState(() {
          javiery = initialPos - height;
        });
      }
    });
  }

  void walkL() {
    direction = "left";
    damage();
    setState(() {
      javierx -= 0.08;
    });
  }

  void walkR() {
    direction = "right";
    damage();
    setState(() {
      javierx += 0.08;
    });
  }

  @override
  Widget build(BuildContext context) {
    if (!clockInitialized) {
      clockTimer();
      clockInitialized = true;
    }
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Column(children: [
        Container(
          color: Colors.blue,
          child:
              Row(mainAxisAlignment: MainAxisAlignment.spaceEvenly, children: [
            Text("Vida: ${health}",
                style: TextStyle(color: Colors.white, fontSize: 20)),
            Text("Modenas: ${score}",
                style: TextStyle(color: Colors.white, fontSize: 20)),
            Text("Tiempo: ${clock}",
                style: TextStyle(color: Colors.white, fontSize: 20))
          ]),
        ),
        Container(
          color: Colors.blue,
          child: Row(mainAxisAlignment: MainAxisAlignment.center, children: [
            Text("GAME OVER",
                style: TextStyle(
                    color: clock == 0 ? Colors.white : Colors.blue,
                    fontSize: 40))
          ]),
        ),
        Expanded(
            flex: 4,
            child: Container(
                color: Colors.blue,
                child: Row(children: [
                  Expanded(
                      child: Container(
                          alignment: Alignment(mariox, marioy),
                          child: Mario())),
                  Expanded(
                      child: AnimatedContainer(
                          alignment: Alignment(javierx, javiery),
                          duration: Duration(milliseconds: 0),
                          child: Javier(
                            direction: direction,
                          ))),
                ]))),
        Container(height: 10, color: Colors.green),
        Expanded(
            flex: 1,
            child: Container(
                color: Colors.brown,
                child: Row(
                    mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                    children: [
                      GestureDetector(
                          onTap: walkL,
                          child: Container(
                            padding: EdgeInsets.all(10),
                            color: Colors.brown[300],
                            child: Icon(Icons.arrow_back),
                          )),
                      GestureDetector(
                          onTap: jump,
                          child: Container(
                            padding: EdgeInsets.all(10),
                            color: Colors.brown[300],
                            child: Icon(Icons.arrow_upward),
                          )),
                      GestureDetector(
                          onTap: walkR,
                          child: Container(
                              padding: EdgeInsets.all(10),
                              color: Colors.brown[300],
                              child: Icon(Icons.arrow_forward))),
                    ])))
      ]),
    );
  }
}

class Javier extends StatelessWidget {
  final direction;

  Javier({this.direction});

  @override
  Widget build(BuildContext context) {
    if (direction == "right") {
      return Container(
          width: 50,
          height: 50,
          child: Image.network(
              "https://lh3.googleusercontent.com/drive-viewer/AJc5JmRWBKrE9XLEYhTNDzeD0TObPYDIZvdScUnD19uSYt7J1aRVvby2N9Sn7EXfNgA4h3gw2p4dHTo=w1600-h700"));
    } else {
      return Transform(
          alignment: Alignment.center,
          transform: Matrix4.rotationY(pi),
          child: Container(
              width: 50,
              height: 50,
              child: Image.network(
                  "https://lh3.googleusercontent.com/drive-viewer/AJc5JmRWBKrE9XLEYhTNDzeD0TObPYDIZvdScUnD19uSYt7J1aRVvby2N9Sn7EXfNgA4h3gw2p4dHTo=w1600-h700")));
    }
  }
}

class Mario extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Container(
        width: 50,
        height: 50,
        child: Image.network(
            "https://cdn.pixabay.com/photo/2021/02/11/15/40/mario-6005703_960_720.png"));
  }
}
