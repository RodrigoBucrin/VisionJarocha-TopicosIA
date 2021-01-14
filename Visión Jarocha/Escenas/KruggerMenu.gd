extends KinematicBody2D

var Game=0
export (PackedScene) var scn1
export (PackedScene) var scn2
export (PackedScene) var scn3

#const GRAVITY = 500.0
const WALK_SPEED = 300
#const JUMP_SPEED=100

var velocity = Vector2()

func _physics_process(delta):
#	velocity.y += delta * GRAVITY
	
		
	if Input.is_action_pressed("ui_left"):
		velocity.x = -WALK_SPEED
	elif Input.is_action_pressed("ui_right"):
		velocity.x =  WALK_SPEED
#	elif Input.is_action_pressed("ui_up"):
#		velocity.y = -JUMP_SPEED
#	elif Input.is_action_pressed("ui_down"):
#		velocity.y = JUMP_SPEED
	else:
		velocity.x =  0

	move_and_slide(velocity, Vector2(0, -1))
	print(Game)
	
	if Input.is_action_pressed("MANODERECHA") and Game==1:
		get_tree().change_scene_to(scn1)
	if Input.is_action_pressed("MANODERECHA") and Game==2:
		get_tree().change_scene_to(scn2)
	if Input.is_action_pressed("MANODERECHA") and Game==3:
		get_tree().change_scene_to(scn3)



func _on_1RA_body_shape_entered(body_id, body, body_shape, area_shape):
	$"../1RA/ColorRect".visible=true
	Game=1

func _on_1RA_body_shape_exited(body_id, body, body_shape, area_shape):
	$"../1RA/ColorRect".visible=false
	Game=0


func _on_2DA_body_shape_entered(body_id, body, body_shape, area_shape):
	$"../2DA/ColorRect".visible=true
	Game=2


func _on_2DA_body_shape_exited(body_id, body, body_shape, area_shape):
	$"../2DA/ColorRect".visible=false
	Game=0


func _on_3RA_body_shape_entered(body_id, body, body_shape, area_shape):
	$"../3RA/ColorRect".visible=true
	Game=3

func _on_3RA_body_shape_exited(body_id, body, body_shape, area_shape):
	$"../3RA/ColorRect".visible=false
	Game=0

