/*
 * File: Keyboard.java
 * ======================================================================
 * A program that displays a keyboard that the user can play!
 */

import java.applet.*;
import java.awt.*;
import java.awt.event.*;
import java.util.*;
import java.io.*;
import acm.program.*;
import acm.util.*;
import acm.graphics.*;

public class KeyboardSolution extends GraphicsProgram {
	/* A nice window size. */
	public static final int APPLICATION_WIDTH = 700;
	public static final int APPLICATION_HEIGHT = 235;

	/* The file containing the keyboard layout. */
	private static final String KEYBOARD_FILE = "keyboardC.txt";
	
	String[] COL_NAMES = {"noteName","x","y","width","height","isWhite","computerKey"};
	
	private HashMap<GRect, AudioClip> noteMap = 
			new HashMap<GRect, AudioClip>();

	public void run() {
		loadKeyboard();
		addMouseListeners();
	}


	public void mousePressed(MouseEvent e) {
		unhighlightKeys();
		GRect hit = (GRect) getElementAt(e.getX(), e.getY());
		if (hit != null) {
			playKey(hit);
		}
	}

	private void unhighlightKeys() {
		for(GRect key : noteMap.keySet()) {
			if(key.getFillColor() == Color.BLUE) {
				key.setFilled(false);
			}
		}
	}

	private void playKey(GRect hit) {
		AudioClip note = noteMap.get(hit);
		note.stop();
		note.play();
		highlightKey(hit);
	}


	private void highlightKey(GRect hit) {
		if(!hit.isFilled()) {
			hit.setFilled(true);
			hit.setFillColor(Color.BLUE);
		}
	}
	
	private void loadKeyboard() {
		try {
			BufferedReader br = new BufferedReader(new FileReader(KEYBOARD_FILE));

			while (true) {
				String line = br.readLine();
				if (line == null) break;
				
				Map<String,String> lineValues = parseLine(line);
				String noteName = lineValues.get("noteName");
				
				GRect key = new GRect(
						Double.parseDouble(lineValues.get("x")),
						Double.parseDouble(lineValues.get("y")),
						Double.parseDouble(lineValues.get("width")),
						Double.parseDouble(lineValues.get("height")));
				if (lineValues.get("isWhite").equals("false")) {
					key.setFilled(true);
				}
				
				add(key);
				noteMap.put(key, MediaTools.loadAudioClip(noteName));
			}
			br.close();			
		} catch (IOException e) {
			println("Duh duh duh duhhhhhh.");
		}
	}


	private Map<String, String> parseLine(String line) {
		String[] elems = line.split(",");
		Map<String, String> values = new HashMap<String, String>();
		for(int i = 0; i < COL_NAMES.length; i++) {
			values.put(COL_NAMES[i], elems[i]);
		}
		return values;
	}
}