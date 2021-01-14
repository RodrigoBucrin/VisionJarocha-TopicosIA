extends KinematicBody2D

const WALK_SPEED = 300
var velocity = Vector2()

func _physics_process(delta):
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


func _on_ENEMIGO1_body_entered(body):
	get_tree().reload_current_scene()


func _on_Area2D_body_entered(body):
	get_tree().reload_current_scene()


func _on_HACKS_body_entered(body):
	$"../Position2D".global_position
